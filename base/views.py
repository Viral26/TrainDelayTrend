from datetime import datetime

from django.shortcuts import render
from matplotlib import pyplot as plt

from .models import main, station_mapping

def train_no(request):
    train_no = ''
    station_code=''
    is_submit=False

    dbTrainList = main.objects.values_list('train_no').distinct().order_by('train_no')
    dbStationCode = main.objects.values_list('station_code').distinct().order_by('station_code')
    dbStationName = dict(station_mapping.objects.values_list('station_code','station_name'))

    SDL = []
    for i in dbStationCode:
        if i[0] in dbStationName.keys():
            SDL.append((i[0],dbStationName[i[0]]))
        else:
            SDL.append((i[0],))

    # print(SDL)
    context={
                'train_no_dropdown':[trainNo[0] for trainNo in dbTrainList],  
                'station_dropdown':SDL,
                'is_submit':is_submit
            }

    if request.method == 'POST':
        train_no = request.POST.get('train_no')
        station_code = request.POST.get('station_code')
        # span = request.POST.get('span')
        # no_of_ticks = 1
        # if span == '1':
        #     no_of_ticks = 1
        # elif span == '2':
        #     no_of_ticks = 1
        # elif span == '3':
        #     no_of_ticks = 2
        # else:
        #     no_of_ticks = 4

        required_records = main.objects.filter(train_no=train_no,station_code=station_code)

        if required_records:
            is_submit = True
            dates=[]
            delays=[]
            station_name = dbStationName[station_code] if station_code in dbStationName.keys() else station_code

            for row in required_records:
                dates.append(datetime.fromtimestamp(row.date_epoch).strftime("%d-%m-%Y"))
                delay = row.delay
                delays.append(delay)
            
            # print(dates,delays)
            # ax = plt.axes()
            plt.figure(figsize=(16,6.5))
            plt.plot(dates,delays)
            plt.xlabel('Date')
            plt.ylabel('Delay (mins)')
            plt.title(f'Train Delay Trend for {train_no} at {station_name}')
            plt.savefig('static/graph.png')
            

            # xticks = []
            # xticklabels = []
            # for ind,val in enumerate(dates):
            #     if ind%no_of_ticks==0:
            #         xticks.append(ind)
            #         xticklabels.append(val)
            # ax.axes.set_xticks(xticks) 
            # ax.axes.set_xticklabels(xticklabels)

            # yticks = []
            # yticklabels = []
            # for i in delays:
            #     yticks.append(i)
            #     if i == -10:
            #         yticklabels.append('Update NA')
            #     else:
            #         yticklabels.append(i)
            # ax.axes.set_yticks(yticks) 
            # ax.axes.set_yticklabels(yticklabels)

            
            
            # plt.close('all')
            context = {
                        'train_no_dropdown':[trainNo[0] for trainNo in dbTrainList],
                        'station_dropdown':SDL,
                        'is_submit':is_submit
                      }

        else:
            context = {
                        'show_error':'Train data does not exist.',
                        'train_no_dropdown':[trainNo[0] for trainNo in dbTrainList],
                        'station_dropdown':SDL,
                        'is_submit':is_submit
                      }

    return render(request,'home.html',context)


def full_status(request):

    train_no = ''
    start_date= ''
    is_submit = False
    context = {}

    dbTrainList = main.objects.values_list('train_no').distinct()

    if request.method == 'POST':
        train_no = request.POST.get('train_no')
        start_date = request.POST.get('start_from_source')
        start_date_epoch = datetime.strptime(start_date,'%Y-%m-%d').timestamp()

        required_records = main.objects.filter(train_no=train_no,start_from_source_epoch=int(start_date_epoch))

        if required_records:
            is_submit = True
            delays=[]
            stations = []

            for row in required_records:
                stations.append(row.station_code)
                delay = row.delay
                delays.append(delay)
                
            plt.figure(figsize=(16,6.5))
            plt.plot(stations,delays)
            plt.xlabel('Stations')
            plt.ylabel('Delay (mins)')
            plt.xticks(rotation=90)
            plt.title(f'Train Delay Trend for {train_no} started on {datetime.fromtimestamp(int(start_date_epoch)).strftime("%d-%m-%Y")}')

            plt.savefig('static/graph1.png')
            plt.cla()

            context = {'is_submit':is_submit,'train_no_dropdown':[trainNo[0] for trainNo in dbTrainList]}
        
        else:
            context={'show_error':'Train data does not exist.'}

    return render(request,'full_status.html',context)
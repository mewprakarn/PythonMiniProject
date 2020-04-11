def gain_lift_chart(target,predict_prob):
    data = pd.DataFrame({'Target':target, 'Predict_prob':predict_prob})
    data_ranked = data.sort_values(['Predict_prob'],ascending=False)

    n = len(data)
    total_target = sum(data.Target)
    event,non_event,total_event,percent_right,percent_wrong,lift_decile = [],[],[],[],[],[]

    for i in np.array_split(data_ranked.Target,10):
        n_event = sum(i)
        n_totalevent = len(i)
        n_non_event = n_totalevent - n_event
        right = n_event/total_target
        wrong = n_non_event/(n-total_target)
        lift = (right/0.1)*100
        
        event.append(n_event)
        total_event.append(n_totalevent)
        non_event.append(n_non_event)
        percent_right.append(right)
        percent_wrong.append(wrong)
        lift_decile.append(lift)

    table = {'Decile':list(range(10,110,10)),
             'Events':event,
             'Non-Events':non_event,
             'Total Events':total_event,
             '% Right':percent_right,
             '% Wrong':percent_wrong 
    }
    
    gain_table = pd.DataFrame(table)
    gain_table['Cum % Right'] = 100*gain_table['% Right'].cumsum()
    gain_table['Cum % Wrong'] = 100*gain_table['% Wrong'].cumsum()
    gain_table['Lift@decile'] = round((gain_table['% Right']/0.1)*100)
    gain_table['Lift'] = round((gain_table['Cum % Right']/gain_table['Decile'])*100)
    
#   plot gain
    plt.figure(figsize=(7,10))
    plt.subplot(311)
    plt.plot(gain_table['Decile'],gain_table['Cum % Right'],label='Model')
    plt.plot(gain_table['Decile'],gain_table['Decile'],color='red',linestyle  ='dashed',label='Random')
    plt.title('Gain Chart')
    plt.xlabel('% Population')
    plt.ylabel('% Target')
    plt.yticks(np.arange(0, 110, step=10))
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.legend()
# plot lift
    plt.subplot(312)
    plt.plot(gain_table['Decile'],gain_table['Lift'],label='Model')
    plt.hlines(100,xmin=10,xmax=100,color='red',linestyles ='dashed',label ='Random')
    plt.title('Lift Chart')
    plt.xlabel('% Population')
    plt.ylabel('% Lift')
    plt.yticks(np.arange(0, 320, step=20))
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.legend()
# Lift @ Decile
    plt.subplot(313)
    plt.plot(gain_table['Decile'],gain_table['Lift@decile'],label='Model')
    plt.hlines(100,xmin=10,xmax=100,color='red',linestyles ='dashed',label ='Random')
    plt.title('Lift@decile Chart')
    plt.xlabel('% Population')
    plt.ylabel('% Lift')
    plt.yticks(np.arange(0, 320, step=20))
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return gain_table

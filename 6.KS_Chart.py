def KS_chart(target,predict_prob):
    data = pd.DataFrame({'Target':target, 'Predict_prob':predict_prob})
    data_ranked = data.sort_values(['Predict_prob'],ascending=False)

    n = len(data)
    total_target = sum(data.Target)
    event,non_event,total_event,percent_right,percent_wrong = [],[],[],[],[]

    for i in np.array_split(data_ranked.Target,10):
        n_event = sum(i)
        n_totalevent = len(i)
        n_non_event = n_totalevent - n_event
        right = n_event/total_target
        wrong = n_non_event/(n-total_target)
        
        event.append(n_event)
        total_event.append(n_totalevent)
        non_event.append(n_non_event)
        percent_right.append(right)
        percent_wrong.append(wrong)


    table = {'Decile':list(range(10,110,10)),
             'Events':event,
             'Non-Events':non_event,
             'Total Events':total_event,
             '% Right':percent_right,
             '% Wrong':percent_wrong 
    }
    ks_table = pd.DataFrame(table)
    ks_table['Cum % Right'] = 100*ks_table['% Right'].cumsum()
    ks_table['Cum % Wrong'] = 100*ks_table['% Wrong'].cumsum()
    ks_table['K-S'] =  ks_table['Cum % Right'] - ks_table['Cum % Wrong']

    
#     plt.figure(figsize=(7,10))
    plt.plot(ks_table['Decile'],ks_table['Cum % Right'],label='%Right')
    plt.plot(ks_table['Decile'],ks_table['Cum % Wrong'],label='%Wrong')
    plt.title('Komogorov-Smirnov Chart')
    plt.xlabel('% Population')
    plt.yticks(np.arange(0, 120, step=20))
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return ks_table

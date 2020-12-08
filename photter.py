import numpy as np
import matplotlib.pyplot as plt
from photJules import photosynthesis

def plotme(x,photo,plotter):
    '''
    plotter utility
    x     :  array to be used for x-axis 
    photo :  photosynthesis data
           
    plotter = {
        n_subplots : 1,       # number of sub-plots
        subplot    : 0,       # index of this sub-plot
        title      : 'title', # subplot title
        name       : 'name',  # plot file name 
        xlabel     : 'x label'# x label             
        log        : False   # use log y scale?
        ymax       : None    # max value for y
    }
    '''
    
    if not plotter:
        return plotter   
    # defaults
    if 'n_subplots' not in plotter:
        plotter['n_subplots'] = 1
    if 'subplot' not in plotter:
        plotter['subplot'] = 0
    if 'ymax' not in plotter:
        plotter['ymax'] = None
    if 'title' not in plotter:
        plotter['title'] = None
    if 'xlabel' not in plotter:
        plotter['xlabel'] = None
    if 'name' not in plotter:
        plotter['name'] = None
    if 'log' not in plotter:
        plotter['log'] = False
    
    if (plotter['subplot'] == 0) \
        or ('fig' not in plotter) \
        or ('axs' not in plotter):
            fig,axs = plt.subplots(plotter['n_subplots'],1,\
                                   figsize=(10,5*plotter['n_subplots']))
            if plotter['n_subplots'] == 1:
                axs = [axs]
            else:
                axs = axs.flatten()
    else:
        axs = plotter['axs']
        fig = plotter['fig']
              
    i = plotter['subplot']
    
    if plotter['log']:
      axs[i].set_yscale('log')

    if plotter['ymax']:
      axs[i].set_ylim(None,plotter['ymax'])
    axs[i].plot( x, photo.Wc * 1e6,label='Wc')
    axs[i].plot( x, photo.Wl * 1e6,label='Wl')
    axs[i].plot( x, photo.We * 1e6,label='We')
    axs[i].plot( x, photo.W * 1e6,label='W')
    axs[i].plot( x, photo.Al* 1e6,label='Al')
    axs[i].plot( x, photo.Rd* 1e6,label='Rd')

    axs[i].set_ylabel('Assimilation rate $(\mu mol\, CO_2 m^{-1} s^{-1})$', fontsize=10)
    if plotter['xlabel'] is None:
        axs[i].set_xlabel('Temperature (C)', fontsize=10)
    else:
        axs[i].set_xlabel(xlabel, fontsize=10)
    if plotter['title']:
        axs[i].set_title(title, fontsize=10)
    else:
        axs[i].set_title(photo.pft[0], fontsize=10)
    axs[i].legend(loc='best', fontsize=10)
    
    # save to file
    if i == plotter['n_subplots'] - 1:
        plotter['filename'] = f"photter_{plotter['name']}.png"
        fig.savefig(plotter['filename'])
        print(f">>> Saved result in {plotter['filename']}")
    else:
        plotter['filename'] = None
        
    plotter['axs'] = axs
    plotter['fig'] = fig
    plotter['subplot'] += 1
    return plotter


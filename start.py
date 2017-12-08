import ipywidgets as ipw

def get_start_widget(appbase, jupbase):
    #http://fontawesome.io/icons/
    template = """
    <table>
    <tr>
        <th style="text-align:center">Tutorials</th>
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center">Corelevel Spectra</th>
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center">Utility</th>
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center">Workflow check</th>
        
    <tr>
    <td valign="top"><ul>
    <li><a href="{appbase}/fleur_tutorial/getting_started.ipynb" target="_blank">Fleur tutorial</a>
    </ul></td>
    
    <td valign="top"><ul>
    <li><a href="{appbase}/corelevel_spectra/Plotting_corelevel_spectra_app.ipynb" target="_blank">all in one</a>
    <li><a href="{appbase}/corelevel_spectra/display.ipynb" target="_blank">display</a>
    <li><a href="{appbase}/corelevel_spectra/compare.ipynb" target="_blank">compare</a>
    <li><a href="{appbase}/corelevel_spectra/search.ipynb" target="_blank">search</a>
    </ul></td>
    
    <td valign="top"><ul>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">Construct slab</a>
    </ul></td>

    <td valign="top"><ul>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">fleur_scf</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">fleur_eos</a>    
    </ul></td>
    </tr></table>
"""
    
    html = template.format(appbase=appbase, jupbase=jupbase)
    return ipw.HTML(html)
    
#EOF

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
        
    <tr>
    <td valign="top"><ul>
    <li><a href="{appbase}/fleur_tutorial/getting_started.ipynb" target="_blank">Fleur tutorial</a>
    <li><a href="{appbase}/fleur_tutorial/getting_started.ipynb" target="_blank">KKR tutorial</a>
    </ul></td>
    
    <td valign="top"><ul>
    <li><a href="{appbase}/corelevel_spectra/display.ipynb" target="_blank">Display Theoretical Spectra</a>
    <li><a href="{appbase}/corelevel_spectra/search.ipynb" target="_blank">Find a Spectrum</a>
    <li><a href="{appbase}/corelevel_spectra/search.ipynb" target="_blank">Fix Stoichiometry</a>
    </ul></td>
    
    <td valign="top"><ul>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">Construct slabs</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">Construct slabs</a>
    </ul></td>

    <tr>
        <th style="text-align:center">Workflow check</th>
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center">Data Explorer</th>
        <th style="width:70px" rowspan=2></th>
    <tr>

    <td valign="top"><ul>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">fleur_scf</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">fleur_eos</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">fleur_relax</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">fleur_dos</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">fleur_band</a>
    </ul></td>
    
    <td valign="top"><ul>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">Find a simulation</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">Structure finder</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">Explorer Phase-space</a>
    <li><a href="{appbase}/slab/build.ipynb" target="_blank">Convex hull of material class</a>
    </ul></td>
    
    
    </tr></table>
"""
    
    html = template.format(appbase=appbase, jupbase=jupbase)
    return ipw.HTML(html)
    
#EOF

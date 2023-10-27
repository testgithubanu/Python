Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> subject ='Art','science','commerce','others'
>>> perc=[25,45,15,15]
>>> explode=(0,0,0.1,0)
>>> plt.pie(perc,explode=explode,labels=subject,autopct='%1.2f%%',shadow=True)
([<matplotlib.patches.Wedge object at 0x000002140279F110>, <matplotlib.patches.Wedge object at 0x000002140279F050>, <matplotlib.patches.Wedge object at 0x0000021403D9C1D0>, <matplotlib.patches.Wedge object at 0x0000021403D9CA70>], [Text(0.7778174593052024, 0.7778174593052024, 'Art'), Text(-1.086457168210212, 0.17207795223283895, 'science'), Text(0.18772129146695624, -1.1852260192596087, 'commerce'), Text(0.9801071672559598, -0.4993895680663526, 'others')], [Text(0.4242640687119285, 0.4242640687119285, '25.00%'), Text(-0.5926130008419338, 0.09386070121791214, '45.00%'), Text(0.10950408668905778, -0.691381844568105, '15.00%'), Text(0.5346039094123416, -0.27239430985437413, '15.00%')])
>>> plt.axis('equal')
(-1.0999946876687658, 1.099999747031846, -1.203706285634274, 1.104938394554013)

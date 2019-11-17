import math
import folium
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

folium_map = folium.Map(location=[53.470, -2.240],
                        zoom_start=18,
                        tiles="CartoDB dark_matter")

marker = folium.CircleMarker(location=[53.470, -2.240], radius = 5)
marker.add_to(folium_map)

folium_map.save("my_map.html")

webbrowser.get(chrome_path).open("my_map.html")

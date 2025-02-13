import shutil
import glob
import os
import time
from pathlib import Path


# # # # # # # # SETUP # # # # # # # # #

target_folder = Path("temp")
#target_folder = "c:/Users/Student/OneDrive - GFN GmbH (EDU)/Dokumente/GitHub/imageOptimizer/backend/temp/"


# Aktuelle Zeit in Var speichern
now = time.time()

# Anzahl der Tage, bis das Verzeichnis gelöscht wird
keep_folder = 1

# Anzahl der Speicherdauer aus keep_folder von der aktuellen Systemzeit abziehen. 
# Berechnung erfolgt in Sekunden (86.400 Sekunden sind 1 Tag)
verzeichnis_del = now - (keep_folder * 86.400)

# Einmal die aktuelle Zeit ausgeben. Das Format verstehe ich noch nicht.
print(now)

# Versuch um mal den Inhalt vom temp anzuzeigen. Deswegen wurde in target_folder aktuell auch der absolute Pfad angegeben, 
# damit überhaupt was angezeigt wird. -> ['6a9bfd90-fefb-4d8f-9c63-1b4788263d3a']
files = os.listdir(target_folder)
print(files)

# Durch alle Unterverzeichnisse iterieren und löschen. Die Prüfung auf das Alter des Verzeichnisses fehlt noch.

#for n in glob.glob('temp/**/', recursive=True):
#    if os.path.isdir(n):
#        shutil.rmtree(n)










# # # # # # Später evtl benötigt # # # # # # # 


#try: shutil.rmtree(directory_path)
#print(f"Directory '{directory_path}' and its contents deleted successfully.")
#except FileNotFoundError: print(f"Directory '{directory_path}' not found.")
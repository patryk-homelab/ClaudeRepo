Sprawdzenie tożsamości eksportu 41393 (MiniPC <-> chmura).
1. BREP: unzip -p 03_.../oryginal/screwdriver_{big,small}.FCStd PartShape.brp > WORKDIR/screwdriver_{big,small}.brp
   (PartShape.brp = bryła Body, ostatnia operacja Pocket004).
2. W calls_export.json zamień WORKDIR na katalog z plikami .brp widoczny w kontenerze build123d-mcp; wywołaj execute + export.
3. Porównaj z sha256_workspace.txt: STL bajt w bajt, 3MF po 3D/3dmodel.model bez wpisu CreationDate.

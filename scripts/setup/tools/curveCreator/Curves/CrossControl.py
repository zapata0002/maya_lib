import maya.cmds as cmds
curve1 = []
curve1.append(cmds.curve( p =[(0.9247539730861667, 0.0, -0.0853561192943805), (0.8937914823092988, 0.0, -0.0853561192943805), (0.8667642029633476, 0.0, -0.06881704668958845), (0.851803335571164, 0.0, -0.044146773561946434), (0.7006966671328105, 0.0, -0.058772842771001636), (0.13625180260677555, 0.0, -0.058772842771001636), (0.05561785869270258, 0.0, -0.058772842771001636), (0.05561785869270258, 0.0, -0.13940687376088676), (0.05561785869270258, 2.819975814072269e-16, -0.7038523478254469), (0.05561785869270258, 2.819975814072269e-16, -0.7844863788153326), (0.0884615291732662, 2.819975814072269e-16, -0.8044038639680093), (0.11048008761708253, 2.819975814072269e-16, -0.8403854298076638), (0.11048008761708253, 2.819975814072269e-16, -0.8816051806074021), (0.11048008761708253, 2.819975814072269e-16, -0.9443654388596857), (0.05960527417398566, 2.819975814072269e-16, -0.9952402523027828), (-0.0031549840782979254, 2.819975814072269e-16, -0.9952402523027828), (-0.06591524233058207, 2.819975814072269e-16, -0.9952402523027828), (-0.11679005577367894, 2.819975814072269e-16, -0.9443654388596857), (-0.11679005577367894, 2.819975814072269e-16, -0.8816051806074021), (-0.11679005577367894, 2.819975814072269e-16, -0.8403893482584122), (-0.09477228102001178, 2.819975814072269e-16, -0.8044077824187577), (-0.06193174530004678, 2.819975814072269e-16, -0.7844863788153326), (-0.06193174530004678, 2.819975814072269e-16, -0.7038523478254469), (-0.06193174530004678, 0.0, -0.13940687376088676), (-0.06193174530004678, 0.0, -0.058772842771001636), (-0.14256534091087003, 0.0, -0.058772842771001636), (-0.707007767282807, 0.0, -0.058772842771001636), (-0.8732833605037653, 0.0, -0.03815596103498406), (-0.8862165497765073, 0.0, -0.05947842481277079), (-0.9095761689377736, 0.0, -0.07377310954160506), (-0.9363369828389415, 0.0, -0.07377310954160506), (-0.9770816168487365, 0.0, -0.07377310954160506), (-1.0101100923805457, 0.0, -0.04074463400979641), (-1.0101100923805457, 0.0, -1.4099879070361346e-15), (-1.0101100923805457, 0.0, 0.04074463400979359), (-0.9770816168487365, 0.0, 0.07377310954160393), (-0.9363369828389415, 0.0, 0.07377310954160393), (-0.909578712838103, 0.0, 0.07377310954160393), (-0.8862190936768365, 0.0, 0.059478424812769666), (-0.873285904404094, 0.0, 0.03815850493531144), (-0.7070112503544923, 0.0, 0.05877676122174773), (-0.14256577628993247, 0.0, 0.05877676122174773), (-0.06193174530004678, 0.0, 0.05877676122174773), (-0.06193174530004678, 0.0, 0.139410356832571), (-0.06193174530004678, -2.819975814072269e-16, 0.7038527832045082), (-0.06193174530004678, -2.819975814072269e-16, 0.784486378815332), (-0.09477619947075958, -2.819975814072269e-16, 0.8044038639680077), (-0.11679397422442701, -2.819975814072269e-16, 0.8403854298076638), (-0.11679397422442701, -2.819975814072269e-16, 0.8816051806074021), (-0.11679397422442701, -2.819975814072269e-16, 0.9443654388596852), (-0.06591916078133014, -2.819975814072269e-16, 0.9952402523027828), (-0.0031589025290462776, -2.819975814072269e-16, 0.9952402523027828), (0.059601355723237305, -2.819975814072269e-16, 0.9952402523027828), (0.11047616916633446, -2.819975814072269e-16, 0.9443654388596852), (0.11047616916633446, -2.819975814072269e-16, 0.8816051806074021), (0.11047616916633446, -2.819975814072269e-16, 0.840389348258411), (0.08845761072251758, -2.819975814072269e-16, 0.8044077824187554), (0.05561785869270258, -2.819975814072269e-16, 0.784486378815332), (0.05561785869270258, -2.819975814072269e-16, 0.7038527832045082), (0.05561785869270258, 0.0, 0.139410356832571), (0.05561785869270258, 0.0, 0.05877676122174773), (0.13625180260677555, 0.0, 0.05877676122174773), (0.7006966671328105, 0.0, 0.05877676122174773), (0.851803335571164, 0.0, 0.044149716876401915), (0.8667671462778064, 0.0, 0.0688170466895862), (0.8937944256237571, 0.0, 0.08535611929437824), (0.9247539730861667, 0.0, 0.08535611929437824), (0.9718958634410065, 0.0, 0.08535611929437824), (1.0101100923805457, 0.0, 0.047141890354839525), (1.0101100923805457, 0.0, -1.4099879070361346e-15), (1.0101100923805457, 0.0, -0.04714189035484122), (0.9718958634410065, 0.0, -0.0853561192943805), (0.9247539730861667, 0.0, -0.0853561192943805)],per = False, d=3, k=[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24]))
fp = cmds.listRelatives(curve1[0], f=True)[0]
path = fp.split("|")[1]
cmds.select(path)
# FLiP-Py-ADS-B

Using Apache Pulsar with ADSB-B Feeds

### Topics to Create (or let be autocreated in Apache Pulsar)

````
bin/pulsar-admin topics create persistent://public/default/adsbraw
````

### Consume Raw Data

````
bin/pulsar-client consume "persistent://public/default/adsbraw" -s adsbrawreader -n 0
````

### Raw JSON Feeds

#### Aircraft

````
{'now': 1659471117.0, 'messages': 7381380, 'aircraft': [{'hex': 'ae6d7a', 'alt_baro': 25000, 'mlat': [], 'tisb': [], 'messages': 177, 'seen': 0.1, 'rssi': -22.7}, {'hex': 'a66174', 'alt_baro': 23000, 'mlat': [], 'tisb': [], 'messages': 5, 'seen': 23.6, 'rssi': -27.8}, {'hex': 'a33a1d', 'flight': 'JBU1267 ', 'alt_baro': 17125, 'alt_geom': 17850, 'gs': 336.0, 'track': 187.7, 'baro_rate': 128, 'squawk': '1146', 'category': 'A3', 'nav_qnh': 1009.6, 'nav_altitude_mcp': 17024, 'nav_modes': ['autopilot', 'althold', 'tcas'], 'lat': 40.341285, 'lon': -74.194169, 'nic': 8, 'rc': 186, 'seen_pos': 9.4, 'version': 2, 'nic_baro': 1, 'nac_p': 10, 'nac_v': 2, 'sil': 3, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 291, 'seen': 5.1, 'rssi': -24.5}, {'hex': 'a4077d', 'alt_baro': 32000, 'alt_geom': 33575, 'gs': 439.1, 'track': 228.1, 'baro_rate': 64, 'nav_qnh': 1013.6, 'nav_altitude_mcp': 32000, 'nav_heading': 0.0, 'lat': 40.791352, 'lon': -74.735621, 'nic': 8, 'rc': 186, 'seen_pos': 42.6, 'version': 2, 'nic_baro': 1, 'nac_p': 9, 'nac_v': 1, 'sil': 3, 'sil_type': 'perhour', 'gva': 2, 'sda': 2, 'mlat': [], 'tisb': [], 'messages': 33, 'seen': 6.1, 'rssi': -24.3}, {'hex': 'ad9ac9', 'category': 'A3', 'version': 0, 'sil_type': 'unknown', 'mlat': [], 'tisb': [], 'messages': 3, 'seen': 122.1, 'rssi': -30.4}, {'hex': 'abef54', 'flight': 'SWA766  ', 'alt_baro': 10150, 'alt_geom': 10450, 'gs': 358.7, 'track': 70.5, 'baro_rate': -64, 'squawk': '6553', 'emergency': 'none', 'category': 'A3', 'nav_qnh': 1008.0, 'nav_altitude_mcp': 10016, 'nav_heading': 85.8, 'lat': 40.440079, 'lon': -74.49585, 'nic': 8, 'rc': 186, 'seen_pos': 0.3, 'version': 2, 'nic_baro': 1, 'nac_p': 9, 'nac_v': 1, 'sil': 3, 'sil_type': 'perhour', 'gva': 2, 'sda': 2, 'mlat': [], 'tisb': [], 'messages': 742, 'seen': 0.0, 'rssi': -11.7}, {'hex': 'a9d90f', 'version': 0, 'sil_type': 'unknown', 'mlat': [], 'tisb': [], 'messages': 6, 'seen': 175.8, 'rssi': -24.9}, {'hex': 'aab2bf', 'flight': 'JBU371  ', 'alt_baro': 20675, 'alt_geom': 21050, 'gs': 412.3, 'track': 190.8, 'baro_rate': 1536, 'category': 'A3', 'lat': 40.07319, 'lon': -74.241735, 'nic': 8, 'rc': 186, 'seen_pos': 2.1, 'version': 2, 'nac_v': 1, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 788, 'seen': 0.5, 'rssi': -21.2}, {'hex': 'aae79d', 'alt_baro': 14925, 'alt_geom': 15275, 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 58, 'seen': 10.6, 'rssi': -24.7}, {'hex': 'ab483c', 'gs': 337.1, 'track': 70.6, 'baro_rate': -192, 'category': 'A3', 'version': 2, 'nac_v': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 1078, 'seen': 67.5, 'rssi': -25.7}, {'hex': 'a6eeb9', 'flight': 'JIA5254 ', 'alt_baro': 18725, 'alt_geom': 19375, 'gs': 321.0, 'track': 228.7, 'geom_rate': 1600, 'category': 'A3', 'nav_qnh': 1008.0, 'nav_altitude_mcp': 19008, 'nav_heading': 241.9, 'lat': 40.440348, 'lon': -74.904286, 'nic': 8, 'rc': 186, 'seen_pos': 17.0, 'version': 2, 'nic_baro': 1, 'nac_p': 10, 'nac_v': 1, 'sil': 3, 'sil_type': 'perhour', 'gva': 2, 'sda': 2, 'mlat': [], 'tisb': [], 'messages': 137, 'seen': 17.0, 'rssi': -21.7}, {'hex': 'a4afbe', 'flight': 'AAL2183 ', 'alt_baro': 34000, 'alt_geom': 35650, 'gs': 431.6, 'track': 227.1, 'baro_rate': 0, 'squawk': '7334', 'emergency': 'none', 'category': 'A3', 'nav_qnh': 1012.8, 'nav_altitude_mcp': 34016, 'lat': 40.436344, 'lon': -74.948668, 'nic': 8, 'rc': 186, 'seen_pos': 1.6, 'version': 2, 'nic_baro': 1, 'nac_p': 9, 'nac_v': 1, 'sil': 3, 'sil_type': 'perhour', 'gva': 2, 'sda': 2, 'mlat': [], 'tisb': [], 'messages': 2268, 'seen': 0.1, 'rssi': -22.3}, {'hex': 'ac2c23', 'alt_baro': 7125, 'alt_geom': 7325, 'gs': 295.6, 'track': 44.2, 'baro_rate': 64, 'squawk': '7267', 'category': 'A3', 'nav_qnh': 1008.0, 'nav_altitude_mcp': 7008, 'nav_modes': ['autopilot', 'althold', 'tcas'], 'lat': 40.439621, 'lon': -74.194641, 'nic': 8, 'rc': 186, 'seen_pos': 4.0, 'version': 2, 'nic_baro': 1, 'nac_p': 10, 'nac_v': 2, 'sil': 3, 'sil_type': 'perhour', 'gva': 2, 'sda': 2, 'mlat': [], 'tisb': [], 'messages': 2064, 'seen': 3.1, 'rssi': -25.7}, {'hex': 'ace19a', 'alt_baro': 22675, 'alt_geom': 23725, 'gs': 416.3, 'track': 261.7, 'baro_rate': -1472, 'category': 'A3', 'version': 2, 'nac_v': 1, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 1097, 'seen': 42.1, 'rssi': -24.0}, {'hex': 'a3cd99', 'alt_baro': 35000, 'alt_geom': 36700, 'gs': 484.5, 'track': 67.9, 'baro_rate': -64, 'category': 'A2', 'nav_qnh': 1012.8, 'nav_altitude_mcp': 35008, 'nav_heading': 80.2, 'lat': 40.269653, 'lon': -73.973328, 'nic': 8, 'rc': 186, 'seen_pos': 11.0, 'version': 2, 'nic_baro': 1, 'nac_p': 10, 'nac_v': 2, 'sil': 3, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 2032, 'seen': 3.9, 'rssi': -23.2}, {'hex': 'a748dd', 'flight': 'N569FG  ', 'alt_baro': 3050, 'alt_geom': 3000, 'gs': 112.3, 'track': 98.7, 'baro_rate': 0, 'squawk': '1200', 'emergency': 'none', 'category': 'A1', 'lat': 40.204607, 'lon': -74.514958, 'nic': 9, 'rc': 75, 'seen_pos': 0.4, 'version': 2, 'nic_baro': 1, 'nac_p': 10, 'nac_v': 2, 'sil': 3, 'sil_type': 'perhour', 'gva': 2, 'sda': 2, 'mlat': [], 'tisb': [], 'messages': 513, 'seen': 0.4, 'rssi': -15.6}, {'hex': 'a8f9f2', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 125, 'seen': 213.7, 'rssi': -22.7}, {'hex': 'a1584a', 'flight': 'EDV4761 ', 'alt_baro': 19225, 'alt_geom': 20100, 'gs': 388.3, 'track': 263.8, 'geom_rate': 2304, 'squawk': '3034', 'emergency': 'none', 'category': 'A3', 'nav_qnh': 1012.8, 'nav_altitude_mcp': 22016, 'nav_heading': 279.1, 'lat': 40.184078, 'lon': -74.730752, 'nic': 8, 'rc': 186, 'seen_pos': 0.5, 'version': 2, 'nic_baro': 1, 'nac_p': 10, 'nac_v': 1, 'sil': 3, 'sil_type': 'perhour', 'gva': 2, 'sda': 2, 'mlat': [], 'tisb': [], 'messages': 3869, 'seen': 0.0, 'rssi': -20.2}, {'hex': 'a823d3', 'category': 'A1', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 257, 'seen': 102.5, 'rssi': -22.9}, {'hex': 'a1d811', 'alt_baro': 31900, 'alt_geom': 33975, 'gs': 468.2, 'track': 39.4, 'baro_rate': -1984, 'squawk': '3023', 'emergency': 'none', 'category': 'A3', 'nav_qnh': 1013.6, 'nav_altitude_mcp': 27008, 'nav_modes': ['autopilot', 'vnav', 'tcas'], 'lat': 40.634354, 'lon': -73.761719, 'nic': 8, 'rc': 186, 'seen_pos': 30.3, 'version': 2, 'nic_baro': 1, 'nac_p': 10, 'nac_v': 2, 'sil': 3, 'sil_type': 'perhour', 'gva': 2, 'sda': 2, 'mlat': [], 'tisb': [], 'messages': 928, 'seen': 26.1, 'rssi': -25.5}, {'hex': 'acd53f', 'version': 0, 'sil_type': 'unknown', 'mlat': [], 'tisb': [], 'messages': 107, 'seen': 7.7, 'rssi': -24.2}, {'hex': 'a6bc31', 'version': 0, 'sil_type': 'unknown', 'mlat': [], 'tisb': [], 'messages': 102, 'seen': 207.9, 'rssi': -25.3}, {'hex': 'aaec3e', 'category': 'A1', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 83, 'seen': 30.9, 'rssi': -24.2}, {'hex': 'ac407d', 'category': 'A3', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 2674, 'seen': 182.5, 'rssi': -22.4}, {'hex': 'aae810', 'category': 'A3', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 4609, 'seen': 116.7, 'rssi': -23.6}, {'hex': 'a7c9f7', 'category': 'A1', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 395, 'seen': 132.6, 'rssi': -24.2}, {'hex': 'accf07', 'category': 'A3', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 1757, 'seen': 224.1, 'rssi': -24.6}, {'hex': 'a203a9', 'category': 'A3', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 813, 'seen': 229.5, 'rssi': -24.1}, {'hex': 'a44197', 'category': 'A3', 'version': 2, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 4460, 'seen': 219.5, 'rssi': -24.8}]}
````

#### Stats

````
{'latest': {'start': 1659470904.3, 'end': 1659470904.3, 'local': {'samples_processed': 0, 'samples_dropped': 0, 'modeac': 0, 'modes': 0, 'bad': 0, 'unknown_icao': 0, 'accepted': [0, 0], 'strong_signals': 0}, 'remote': {'modeac': 0, 'modes': 0, 'bad': 0, 'unknown_icao': 0, 'accepted': [0, 0]}, 'cpr': {'surface': 0, 'airborne': 0, 'global_ok': 0, 'global_bad': 0, 'global_range': 0, 'global_speed': 0, 'global_skipped': 0, 'local_ok': 0, 'local_aircraft_relative': 0, 'local_receiver_relative': 0, 'local_skipped': 0, 'local_range': 0, 'local_speed': 0, 'filtered': 0}, 'altitude_suppressed': 0, 'cpu': {'demod': 0, 'reader': 0, 'background': 0}, 'tracks': {'all': 0, 'single_message': 0, 'unreliable': 0}, 'messages': 0, 'messages_by_df': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, 'last1min': {'start': 1659470844.2, 'end': 1659470904.3, 'local': {'samples_processed': 144048128, 'samples_dropped': 0, 'modeac': 0, 'modes': 1478008, 'bad': 3456520, 'unknown_icao': 603889, 'accepted': [4031, 272], 'signal': -14.9, 'noise': -30.6, 'peak_signal': -3.3, 'strong_signals': 0}, 'remote': {'modeac': 0, 'modes': 0, 'bad': 0, 'unknown_icao': 0, 'accepted': [0, 0]}, 'cpr': {'surface': 0, 'airborne': 405, 'global_ok': 373, 'global_bad': 0, 'global_range': 0, 'global_speed': 0, 'global_skipped': 0, 'local_ok': 25, 'local_aircraft_relative': 0, 'local_receiver_relative': 0, 'local_skipped': 7, 'local_range': 0, 'local_speed': 0, 'filtered': 0}, 'altitude_suppressed': 0, 'cpu': {'demod': 9538, 'reader': 1515, 'background': 400}, 'tracks': {'all': 8, 'single_message': 3, 'unreliable': 3}, 'messages': 4303, 'messages_by_df': [1398, 0, 0, 0, 285, 2, 0, 0, 0, 0, 0, 1409, 0, 0, 0, 0, 65, 1122, 3, 0, 16, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'adaptive': {'gain_db': 42.1, 'dynamic_range_limit_db': 42.1, 'gain_changes': 0, 'loud_undecoded': 0, 'loud_decoded': 0, 'noise_dbfs': -33.7, 'gain_seconds': [[42.1, 60]]}}, 'last5min': {'start': 1659470604.2, 'end': 1659470904.3, 'local': {'samples_processed': 720109568, 'samples_dropped': 0, 'modeac': 0, 'modes': 7483379, 'bad': 17539993, 'unknown_icao': 3057885, 'accepted': [17551, 1126], 'signal': -13.5, 'noise': -29.7, 'peak_signal': -2.5, 'strong_signals': 83}, 'remote': {'modeac': 0, 'modes': 0, 'bad': 0, 'unknown_icao': 0, 'accepted': [0, 0]}, 'cpr': {'surface': 0, 'airborne': 1543, 'global_ok': 1387, 'global_bad': 0, 'global_range': 0, 'global_speed': 0, 'global_skipped': 0, 'local_ok': 110, 'local_aircraft_relative': 0, 'local_receiver_relative': 0, 'local_skipped': 46, 'local_range': 0, 'local_speed': 0, 'filtered': 0}, 'altitude_suppressed': 0, 'cpu': {'demod': 47631, 'reader': 7530, 'background': 1965}, 'tracks': {'all': 39, 'single_message': 20, 'unreliable': 21}, 'messages': 18677, 'messages_by_df': [6632, 0, 0, 0, 1023, 19, 0, 0, 0, 0, 0, 6504, 0, 0, 0, 0, 214, 4220, 11, 0, 46, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'adaptive': {'gain_db': 42.1, 'dynamic_range_limit_db': 42.1, 'gain_changes': 0, 'loud_undecoded': 0, 'loud_decoded': 0, 'noise_dbfs': -33.7, 'gain_seconds': [[42.1, 300]]}}, 'last15min': {'start': 1659470004.2, 'end': 1659470904.3, 'local': {'samples_processed': 2160066560, 'samples_dropped': 0, 'modeac': 0, 'modes': 22605285, 'bad': 53034842, 'unknown_icao': 9242439, 'accepted': [49450, 3033], 'signal': -12.4, 'noise': -29.2, 'peak_signal': -1.9, 'strong_signals': 616}, 'remote': {'modeac': 0, 'modes': 0, 'bad': 0, 'unknown_icao': 0, 'accepted': [0, 0]}, 'cpr': {'surface': 0, 'airborne': 4548, 'global_ok': 4139, 'global_bad': 0, 'global_range': 0, 'global_speed': 0, 'global_skipped': 0, 'local_ok': 285, 'local_aircraft_relative': 0, 'local_receiver_relative': 0, 'local_skipped': 124, 'local_range': 0, 'local_speed': 0, 'filtered': 0}, 'altitude_suppressed': 0, 'cpu': {'demod': 143606, 'reader': 22596, 'background': 5809}, 'tracks': {'all': 95, 'single_message': 52, 'unreliable': 55}, 'messages': 52483, 'messages_by_df': [18442, 0, 0, 0, 2929, 44, 0, 0, 0, 0, 0, 17851, 0, 0, 0, 0, 547, 12522, 27, 0, 112, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'adaptive': {'gain_db': 42.1, 'dynamic_range_limit_db': 42.1, 'gain_changes': 0, 'loud_undecoded': 0, 'loud_decoded': 0, 'noise_dbfs': -33.7, 'gain_seconds': [[42.1, 900]]}}, 'total': {'start': 1659368484.1, 'end': 1659470904.3, 'local': {'samples_processed': 245769699328, 'samples_dropped': 0, 'modeac': 0, 'modes': 2568188151, 'bad': 1750160172, 'unknown_icao': 1042573355, 'accepted': [6936685, 432042], 'signal': -11.8, 'noise': -29.9, 'peak_signal': -0.9, 'strong_signals': 163598}, 'remote': {'modeac': 0, 'modes': 0, 'bad': 0, 'unknown_icao': 0, 'accepted': [0, 0]}, 'cpr': {'surface': 4, 'airborne': 739605, 'global_ok': 694626, 'global_bad': 9, 'global_range': 0, 'global_speed': 7, 'global_skipped': 320, 'local_ok': 34403, 'local_aircraft_relative': 0, 'local_receiver_relative': 0, 'local_skipped': 10571, 'local_range': 0, 'local_speed': 0, 'filtered': 0}, 'altitude_suppressed': 0, 'cpu': {'demod': 16357720, 'reader': 2576911, 'background': 661255}, 'tracks': {'all': 10145, 'single_message': 6130, 'unreliable': 6406}, 'messages': 7368727, 'messages_by_df': [2442857, 0, 0, 0, 454119, 11016, 0, 0, 0, 0, 0, 2321942, 0, 0, 0, 0, 86193, 2032424, 3060, 0, 16145, 971, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'adaptive': {'gain_db': 42.1, 'dynamic_range_limit_db': 42.1, 'gain_changes': 122, 'loud_undecoded': 0, 'loud_decoded': 0, 'noise_dbfs': -33.7, 'gain_seconds': [[38.6, 7220], [40.2, 7417], [42.1, 12842], [43.4, 476], [43.9, 3845], [44.5, 4936], [48.0, 4503], [49.6, 60946], [58.6, 219]]}}}
````

### Aircraft Schema 

````
aircraft
  multiple rows
  
  single row 
  'hex': 'a3cd99', 'alt_baro': 35000, 'alt_geom': 36700, 'gs': 484.5, 'track': 67.9, 'baro_rate': -64, 'category': 'A2', 'nav_qnh': 1012.8, 'nav_altitude_mcp': 35008, 'nav_heading': 80.2, 'lat': 40.269653, 'lon': -73.973328, 'nic': 8, 'rc': 186, 'seen_pos': 11.0, 'version': 2, 'nic_baro': 1, 'nac_p': 10, 'nac_v': 2, 'sil': 3, 'sil_type': 'perhour', 'mlat': [], 'tisb': [], 'messages': 2032, 'seen': 3.9, 'rssi': -23.2
  
  hex (String optional)
  flight (String optional - name of plane)
  alt_baro (int optional - altitude)
  alt_geom (int optional) 
  track (int optional)
  baro_rate (int optional)
  category (string optional)
  nav_qnh (float optional)
  nav_altitude_mcp (int optional)
  nav_heading (float optional)
  nic (int optional)
  rc (int optional)
  seen_pos (float optional)
  version (int optional)
  nic_baro (int optional)
  nac_p (int optional)
  nac_v (int optional)
  sil (int optional) 
  sil_type (string optional)
  mlat (array optional)
  tisb (array optional)
  messages (int optional)
  seen (float optional)
  rssi (float optional)  
  squawk (optional) - look at # conversion 7600, 7700, 4000, 5000, 7777, 6100, 5400, 4399, 4478, ...)
  speed (optional)
  mach (optional speed, mac to mph *767)
  emergency (optional string)
  lat (long optional)
  lon (long optional)
  
  
  
````

### Data Sent

````
pulsar://pulsar1:6650
persistent://public/default/adsbraw

2022-08-02 16:42:25.601 INFO  [3069528448] ClientConnection:182 | [<none> -> pulsar://pulsar1:6650] Create ClientConnection, timeout=10000
2022-08-02 16:42:25.601 INFO  [3069528448] ConnectionPool:96 | Created connection for pulsar://pulsar1:6650
2022-08-02 16:42:25.606 INFO  [3032257600] ClientConnection:368 | [192.168.1.204:39188 -> 192.168.1.230:6650] Connected to broker
2022-08-02 16:42:25.611 INFO  [3032257600] HandlerBase:64 | [persistent://public/default/adsbraw-partition-0, ] Getting connection from pool
2022-08-02 16:42:25.613 INFO  [3032257600] ClientConnection:182 | [<none> -> pulsar://pulsar1:6650] Create ClientConnection, timeout=10000
2022-08-02 16:42:25.613 INFO  [3032257600] ConnectionPool:96 | Created connection for pulsar://127.0.0.1:6650
2022-08-02 16:42:25.618 INFO  [3032257600] ClientConnection:370 | [192.168.1.204:39190 -> 192.168.1.230:6650] Connected to broker through proxy. Logical broker: pulsar://127.0.0.1:6650
2022-08-02 16:42:25.625 INFO  [3032257600] ProducerImpl:189 | [persistent://public/default/adsbraw-partition-0, ] Created producer on broker [192.168.1.204:39190 -> 192.168.1.230:6650]
Sent aircraft data: 10068
Sent aircraft data: 10106
Sent aircraft data: 9836
Sent aircraft data: 9833
Sent aircraft data: 9834
Sent aircraft data: 9831
Sent aircraft data: 9829
Sent aircraft data: 10011
Sent aircraft data: 9953
Sent aircraft data: 9955
Sent aircraft data: 9937
Sent aircraft data: 9935
Sent aircraft data: 9933
^C2022-08-02 16:41:53.892 INFO  [3069352320] ClientImpl:495 | Closing Pulsar client with 1 producers and 0 consumers
2022-08-02 16:41:53.892 INFO  [3069352320] ProducerImpl:686 | [persistent://public/default/adsbraw-partition-0, standalone-1-70] Closing producer for topic persistent://public/default/adsbraw-partition-0
2022-08-02 16:41:53.895 INFO  [3032081472] ProducerImpl:729 | [persistent://public/default/adsbraw-partition-0, standalone-1-70] Closed producer
2022-08-02 16:41:53.895 INFO  [3032081472] ClientConnection:1548 | [192.168.1.204:39050 -> 192.168.1.230:6650] Connection closed
2022-08-02 16:41:53.895 INFO  [3032081472] ClientConnection:1548 | [192.168.1.204:39048 -> 192.168.1.230:6650] Connection closed
````

### Data parsed by Pulsar Function and sent to persistent://public/default/aircraft

````
bin/pulsar-client consume "persistent://public/default/aircraft" -s "aircraftconsumer" -n 0

----- got message -----
key:[178cbf7b-f52d-4a7f-b072-dfef8b53fa8a], properties:[language=Java], content:{"flight":"N816SR","category":"A1","emergency":"none","squawk":1540,"hex":"ab2146","gs":170.8,"track":199.5,"lat":40.163409,"lon":-74.753411,"nic":9,"rc":75,"version":2,"sil":3,"gva":2,"sda":2,"mlat":[],"tisb":[],"messages":2291,"seen":0.8,"rssi":-18.5}
----- got message -----
key:[0677e81a-57f1-41a5-96c3-f57277498c79], properties:[language=Java], content:{"flight":"N333BD","category":"A1","emergency":"none","squawk":1352,"hex":"a3a111","gs":377.8,"track":226.9,"lat":40.160706,"lon":-75.335388,"nic":9,"rc":75,"version":2,"sil":3,"gva":2,"sda":2,"mlat":[],"tisb":[],"messages":4830,"seen":0.6,"rssi":-21.1}
----- got message -----
key:[c480cd8e-a803-47fe-81b4-aafdec0f6b68], properties:[language=Java], content:{"flight":"N86HZ","category":"A7","emergency":"none","squawk":1200,"hex":"abcd45","gs":52.2,"track":106.7,"lat":40.219757,"lon":-74.580566,"nic":9,"rc":75,"version":2,"sil":3,"gva":2,"sda":2,"mlat":[],"tisb":[],"messages":2259,"seen":1.1,"rssi":-19.9}

````

### Functions

#### See Function
* https://github.com/tspannhw/pulsar-adsb-function


````
bin/pulsar-admin functions status --name ADSB


bin/pulsar-admin functions stop --name ADSB --namespace default --tenant public
bin/pulsar-admin functions delete --name ADSB --namespace default --tenant public

bin/pulsar-admin functions create --auto-ack true --jar /opt/demo/java/pulsar-adsb-function/target/adsb-1.0.jar --classname "dev.pulsarfunction.adsb.ADSBFunction" --dead-letter-topic "persistent://public/default/adsbdead" --inputs "persistent://public/default/adsbraw" --log-topic "persistent://public/default/adsblog" --name ADSB --namespace default --tenant public --max-message-retries 5


````


### References

* https://flightaware.com/adsb/piaware/build/
* https://flightaware.com/adsb/stats/user/TimothySpann
* https://github.com/adsbxchange/dump1090-fa
* https://flightaware.com/adsb/piaware/build
* https://flightaware.com/adsb/piaware/build/optional#piawarecommands
* https://dzone.com/articles/ingesting-flight-data-ads-b-usb-receiver-with-apac
* https://globe.adsbexchange.com/
* https://community.cloudera.com/t5/Community-Articles/Ingesting-Flight-Data-ADS-B-USB-Receiver-with-Apache-NiFi-1/ta-p/247940
* https://elmwoodelectronics.ca/blogs/news/tracking-and-logging-flights-with-ads-b-flight-aware-and-raspberry-pi
* https://github.com/flightaware/piaware

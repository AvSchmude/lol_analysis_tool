import re

TABLES = {'items': (
    "CREATE TABLE items ("
    "   id INTEGER NOT NULL,"
    "   name VARCHAR(50) NOT NULL,"  # nr['name']
    "   cost INTEGER NOT NULL"       # nr['gold']['total']
    "   text VARCHAR(255),"          # nr['plaintext']
    "   PRIMARY KEY(id)"
    ") ENGINE=InnoDB"), 'participants': (
    "   CREATE TABLE participants("
    "   id INTEGER NOT NULL AUTO_INCREMENT,"
    "   name VARCHAR(25) NOT NULL,"
    "   team_colour VARCHAR(4) NOT NULL,"
    "   champion VARCHAR(25) NOT NULL,"
    "   champion_level INTEGER NOT NULL,"
    "   position VARCHAR(10) NOT NULL,"
    "   kills INTEGER NOT NULL,"
    "   deaths INTEGER NOT NULL,"
    "   assists INTEGER NOT NULL,"
    "   creep_score INTEGER NOT NULL,"
    "   gold_earned INTEGER NOT NULL,"
    "   win BOOLEAN NOT NULL, "
    "   minions_killed INTEGER NOT NULL,"
    "   monsters_killed INTEGER NOT NULL,"
    "   damage_dealt_total INTEGER NOT NULL,"
    "   damage_dealt_physical INTEGER NOT NULL,"
    "   damage_dealt_magical INTEGER NOT NULL,"
    "   damage_dealt_true INTEGER NOT NULL,"
    "   damage_taken_total INTEGER NOT NULL,"
    "   damage_taken_physical INTEGER NOT NULL,"
    "   damage_taken_magical INTEGER NOT NULL,"
    "   damage_taken_true INTEGER NOT NULL,"
    "   healing_total INTEGER NOT NULL,"
    "   healing_teammates INTEGER NOT NULL,"
    "   shielding_teammates INTEGER NOT NULL,"
    "   vision_score INTEGER NOT NULL,"
    "   wards_placed INTEGER NOT NULL,"
    "   pinks_placed INTEGER NOT NULL,"
    "   wards_killed INTEGER NOT NULL,"
    "   turret_kills INTEGER NOT NULL,"
    "   longest_time_alive INTEGER NOT NULL,"
    "   spell_count_q INTEGER NOT NULL,"
    "   spell_count_w INTEGER NOT NULL,"
    "   spell_count_e INTEGER NOT NULL,"
    "   spell_count_r INTEGER NOT NULL,"
    "   ping_count INTEGER NOT NULL,"
    "   item1_id INTEGER,"
    "   item2_id INTEGER,"
    "   item3_id INTEGER,"
    "   item4_id INTEGER,"
    "   item5_id INTEGER,"
    "   item6_id INTEGER,"
    "   PRIMARY KEY (id),"
    "   CONSTRAINT ck_win_bool CHECK (win in (1,0)),"
    "   FOREIGN KEY(item1_id) REFERENCES items(id),"
    "   FOREIGN KEY(item2_id) REFERENCES items(id),"
    "   FOREIGN KEY(item3_id) REFERENCES items(id),"
    "   FOREIGN KEY(item4_id) REFERENCES items(id),"
    "   FOREIGN KEY(item5_id) REFERENCES items(id),"
    "   FOREIGN KEY(item6_id) REFERENCES items(id)"
    "   )"), 'matches': (
    "CREATE TABLE matches("
    "   id INTEGER NOT NULL,"
    "   date DATE NOT NULL,"
    "   type VARCHAR(25),"
    "   patch VARCHAR(25),"
    "   platform VARCHAR(25),"
    "   duration FLOAT(10),"
    "   part1_id INTEGER NOT NULL,"
    "   part2_id INTEGER NOT NULL,"
    "   part3_id INTEGER NOT NULL,"
    "   part4_id INTEGER NOT NULL,"
    "   part5_id INTEGER NOT NULL,"
    "   part6_id INTEGER NOT NULL,"
    "   part7_id INTEGER NOT NULL,"
    "   part8_id INTEGER NOT NULL,"
    "   part9_id INTEGER NOT NULL,"
    "   part10_id INTEGER NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY(part1_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part2_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part3_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part4_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part5_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part6_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part7_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part8_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part9_id) REFERENCES participants(id),"
    "   FOREIGN KEY(part10_id) REFERENCES participants(id)"
    ") ENGINE=InnoDB")}


def find_with_regex(query):
    word_list = ['VARCHAR', 'INTEGER', 'FLOAT', 'DATE']
    pattern = rf'(\w+)\s*(?:\b(?:{"|".join(word_list)})\b)'
    keyword = re.findall(pattern, query)
    return keyword


item_keywords = find_with_regex(TABLES['items'])
part_keywords = find_with_regex(TABLES['participants'])
match_keywords = find_with_regex(TABLES['matches'])

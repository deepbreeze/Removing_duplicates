import csv,sqlite3
# Remove the space lines from the rawfile
ffile = open('output_1.txt','w').writelines([l for l in open('output.txt','r').readlines()if l[:-1].strip()])
    
con = sqlite3.connect(":memory:")
con.text_factory = str
cur = con.cursor()

# Create the table
cur.execute('DROP TABLE IF EXISTS t')
cur.execute('CREATE TABLE t (Email text)')
con.commit()

# Load the txt file into creader
csvfile = open('output_1.txt','rb')
creader = csv.reader(csvfile)

for l in creader:
    cur.execute('INSERT INTO t VALUES (?)',l)


data = cur.execute('SELECT DISTINCT Email FROM t')

# Write data to txt
with open ('Newfile.txt','wb') as f:
    writer = csv.writer(f)
    writer.writerow(['Email'])
    writer.writerows(data)
    
f.close()
csvfile.close()
con.commit()
con.close()
    

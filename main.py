import csv

file_contents = open('NamelessRP Data - Sheet1.csv', newline='')

data = csv.reader(file_contents)
row_num=0
output={}
for row in data:
    col_num=0
    for cell in row:
        if col_num%2==0 and row_num==0:
            output[str(int(col_num/2))]={'id':str(cell)}
        else:
            if col_num%2==1:
                output[str(int((col_num-1)/2))][row[col_num-1]]=cell
            
        #print("Row: "+str(row_num)+" | Column: "+str(col_num)+" | Data: ",cell)
        col_num+=1
    row_num+=1

ExpressionFirst='@name Creates a List of Global Tables that e2s can access\nif(first()){'
ExpressionEnding='\n#E2 designed by Pie'
for table in output:
    table_data=output[table]
    ExpressionFirst+='\n    timer("'+table+'",'+str(1000*int(table))+')'
    ExpressionEnding+='\nif(clk("'+table+'")){'
    ExpressionEnding+='{0}G=gTable("'.format('\n    ')+table_data['id']+'",1)'
    for key in table_data:
        if key != 'id' and key != table_data['id']:
            ExpressionEnding+=('{0}G["'+key+'",string] = "'+table_data[key]+'"').format('\n    ')
    ExpressionEnding+='\n}\n'
    #print(output[table])
SelfDestruct=len(output)
ExpressionFirst+='\n    timer("'+str(SelfDestruct)+'",'+str(1000*int(SelfDestruct))+')'
ExpressionFirst+='\n}'
ExpressionEnding+='\nif(clk("'+str(SelfDestruct)+'")){'
ExpressionEnding+='{0}print("Pie\'s global table e2 has finished generating, chip is being deleted")'.format('\n    ')
ExpressionEnding+='{0}selfDestruct()'.format('\n    ')
ExpressionEnding+='\n}'
FullE2=ExpressionFirst+ExpressionEnding
print(FullE2)
text_file = open("output.txt", "w")
text_file.write(FullE2)
text_file.close()
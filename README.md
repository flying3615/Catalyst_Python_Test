# Response to script&logic tasks
## In terms of script task
- Need MySQLdb module support, `pip install MySQL-python`
- There are two branches dev/master, have been working on dev and merge it to master.
- I reuse my docker wordpress env to simulate mysql server, so that I assume the DB name is *wordpress*
- CSV content of three columns can be in any order, as I record each index of them
- Ignored blank lines in CSV file
- Any records with invalid email cannot be inserted into DB 
- INSERT statements are dynamically generated, if it's not dry-run, *Done* will be printed out at the end to indicate it's been inserted
  INSERT INTO users (name,surname,email) VALUES ("John","Smith","jsmith@gmail.com")  *Done*
- The result of running the script also has been handled, "1" is abnormal
- DB final result should be: 
>1	John	Smith	jsmith@gmail.com  
2	Hamish	Jones	ham@seek.com  
3	Phil	Carry	phil@open.edu.au  
4	Johnny	O'Hare	john@yahoo.com.au  
5	Mike	O'Connor	mo'connor@cat.net.nz  
6	William	Smythe	happy@ent.com.au  
8	Sam!!	Walters	sam!@walters.org  
9	Daley	Thompson	daley@yahoo.co.nz  
10	Kevin	Ruley	kevin.ruley@gmail.com  
SELECT Person.firstName, Person.lastName, Address.city, Address.state 
from Person
left join Address ON Person.personId = Address.personId;  


#it is the most optimized way to do it


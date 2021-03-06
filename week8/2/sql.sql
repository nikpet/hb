SELECT FirstName, LastName, Title FROM Employees;
SELECT * FROM Employees WHERE City = 'Seattle';
SELECT * FROM Employees WHERE City = 'London';
SELECT * FROM Employees WHERE Title LIKE '%Sales%';
SELECT * FROM Employees WHERE Title LIKE '%Sales%' AND (TitleOfCourtesy = 'Ms.' OR TItleOfCourtesy = 'Mrs.');
SELECT * FROM Employees ORDER BY BirthDate ASC LIMIT 5;
SELECT * FROM Employees ORDER BY HireDate ASC LIMIT 5;
SELECT * FROM Employees WHERE ReportsTo IS NULL;
SELECT e1.FirstName, e1.LastName, e2.FirstName, e2.LastName FROM Employees AS e1 JOIN Employees AS e2 ON e1.ReportsTo = e2.EmployeeID;
SELECT COUNT(*) FROM Employees WHERE TitleOfCourtesy = 'Ms.' OR TItleOfCourtesy = 'Mrs.';
SELECT COUNT(*) FROM Employees WHERE TitleOfCourtesy != 'Ms.' AND TItleOfCourtesy != 'Mrs.';
SELECT COUNT(*), City FROM Employees GROUP BY City;
SELECT OrderID, FirstName, LastName From Employees as e JOIN Orders as o ON o.EmployeeID = e.EmployeeID;
SELECT OrderID, CompanyName FROM Orders as o JOIN Shippers as s ON o.ShipVia = s.ShipperID;
SELECT Country, Count(Orders.OrderID) FROM Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID GROUP BY Country;
SELECT FirstName, LastName, COUNT(FirstName) cnt From Employees JOIN Orders ON Orders.EmployeeID = Employees.EmployeeID GROUP BY FirstName, LastName ORDER BY cnt DESC LIMIT 1;
SELECT ContactName, COUNT(ContactName) cnt FROM Customers JOIN Orders ON Orders.CustomerID = Customers.CustomerID GROUP BY ContactName ORDER BY cnt DESC LIMIT 1;
SELECT o.OrderID, e.Firstname, e.LastName, c.CompanyName FROM Employees as e JOIN Orders as o ON o.EmployeeID = e.EmployeeID JOIN Customers AS c ON o.CustomerID = c.CustomerID;
SELECT c.CompanyName, s.CompanyName FROM Orders as o JOIN Customers as c ON o.CustomerID = c.CustomerID JOIN Shippers as s ON o.ShipVia = s.ShipperID;
SELECT OrderID, CompanyName FROM Orders as o JOIN Shippers as s ON o.ShipVia = s.ShipperID;

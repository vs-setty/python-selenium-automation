# Created by vyshnavisomisetty at 10/11/22
 Feature:Tests for amazon add to cart

  Scenario: User can add product to cart
   Given Open Amazon page
   When Search for Tritan Farm to Table Pitcher on Amazon
   And Click on the first product
   And Click on Add to cart button
   And Open cart page
   Then Verify cart has 1 item(s)


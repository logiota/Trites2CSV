# Trytes2CSV
Translate trytes directly to alphanumeric characters and keep the trytes somewhat readable directly in a tangle explorer.

This will help run projects on small devices doing datalogging by reducing the pow for larger than 440 Bytes of data.

A csv file in a single transaction can now contain 670 double digit measurements or at least 2000 characters.

This is an example of data turnary:
XFL9XCLAY9XCOUNTY9BFEHBAJEG9O9AEGEO

Which should result in the following ASCII data:
FL,CLAY COUNTY,265821.57,0,15750

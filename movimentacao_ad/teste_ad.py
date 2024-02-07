import os

os.system('Get-ADUser -Filter * -Property * | Select-Object Name, DistinguishedName, UserPrincipalName, Enabled | Export-Csv -Path "C:\Users\guaca.infran1\Desktop\USER_AD.csv" -NoTypeInformation')
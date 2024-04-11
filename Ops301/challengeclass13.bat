# Script Name:                  Ops Challenge - Powershell AD Automation
# Author:                       Gilbert Collado
# Date of latest revision:      04/10/2024
# Purpose:                      Create a script that uses library requests
# Source1:                      https://github.com/codefellows/seattle-ops-301d12/blob/main/class-13/challenges/DEMO.md
# Source2:                      https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2019-ps

# Define user details
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$userPrincipalName = "ferdi@GlobeXpower.com"
$office = "Springfield"
$department = "TPS"
$title = "TPS Reporting Lead"
$email = "ferdi@GlobeXpower.com"
$password = "P@ssw0rd123" # You should generate a strong password and replace this

# Set AD attributes
$ADAttributes = @{
    GivenName = $firstName
    Surname = $lastName
    DisplayName = $displayName
    UserPrincipalName = $userPrincipalName
    SamAccountName = $userPrincipalName.Split("@")[0]
    Office = $office
    Department = $department
    Title = $title
    EmailAddress = $email
    AccountPassword = (ConvertTo-SecureString -String $password -AsPlainText -Force)
    Enabled = $true
}

# Create the user in Active Directory
New-ADUser @ADAttributes -PassThru

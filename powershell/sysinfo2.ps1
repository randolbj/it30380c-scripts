#$Hello = "Hello, Powershell!"
#write-Host($Hello)

function getIP {
    (Get-NetIPAddress).IPv4Address | select-string "192*"
}

write-host(getIP)
$IP = getIP
write-host("This machines IP is $IP")
write-host("This machines IP is {0}" -f $IP)

$Date = " "
$Body = "this machines IP is $IP. user is $env:username. Hostname is $. PwerShell Version . Todays date is $Date"
write-host($Body)

#Send-MailMessage -To "randolbj@mail.uc.edu" From "brando.rando17@gmail.com" -Subject "IT3080C sysinfo" -Body $Body -SmtpServer smtp.google.com -Port 587 -UseSSL -Credential (Get-Credential)
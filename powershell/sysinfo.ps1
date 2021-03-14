#$Hello = "Hello, Powershell!"
#write-Host($Hello)

function getIP {
    (Get-NetIPAddress).IPv4Address | select-string "192*"
}

write-host(getIP)
$IP = getIP
write-host("This machines IP is $IP")
write-host("This machines IP is {0}" -f $IP)

$Date = 
$Body = "this machines IP is $IP. user is $env:username. Hostname is $. PwerShell Version $Host.Version.Major. Todays date is $Date"

send-MailMessage -To "randolbj@mail.uc.edu" from "randolbj@mail.uc.edu" -subject "IT3080C sysinfo" -body $Body -smtpServer smtp.google.com -port 587 -useSSL -credentials (Get-Credential)


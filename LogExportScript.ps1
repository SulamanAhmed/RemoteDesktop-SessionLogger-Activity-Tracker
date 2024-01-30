<#
    UserActivityTracking.ps1

    Description:
    A PowerShell script to track user activity on Windows 10/11 systems,
    focusing on login and logout times during Remote Desktop sessions.
 
#>

param (
   <#[string]$dateParam = '2024-01-29'#>
	$dateParam = (Get-Date).ToString("yyyy-MM-dd")
)

Write-Host "Script started. Target date: $dateParam"

$targetDate = [DateTime]::ParseExact($dateParam, "yyyy-MM-dd", $null)
$detailedCsvFilePath = "C:\Users\akhan\Desktop\output-detailed-$dateParam.csv"
$startTime = $targetDate.Date
$endTime = $targetDate.Date.AddDays(1)

Write-Host "Detailed CSV File Path: $detailedCsvFilePath"
Write-Host "Time range: $startTime to $endTime"

function SafeGet-WinEvent {
    param (
        [hashtable]$FilterHashtable,
        [int]$MaxEvents = 1000
    )
    try {
        $events = Get-WinEvent -FilterHashtable $FilterHashtable -MaxEvents $MaxEvents -ErrorAction Stop
    } catch {
        Write-Host "Error fetching events: $_"
        $events = @()
    }
    return $events
}

$logonEvents = SafeGet-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-LocalSessionManager/Operational'; ID=21; StartTime=$startTime; EndTime=$endTime}
$logoffAndDisconnectEvents = SafeGet-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-LocalSessionManager/Operational'; ID=23,24,25,40; StartTime=$startTime; EndTime=$endTime}

Write-Host "Logon Events Count: $($logonEvents.Count)"
Write-Host "Logoff and Disconnect Events Count: $($logoffAndDisconnectEvents.Count)"

# Combine logon and logoff events
$allEvents = $logonEvents + $logoffAndDisconnectEvents

# Export all events to detailed CSV
$allEvents | Select-Object TimeCreated, Id, Message | Export-Csv -Path $detailedCsvFilePath -NoTypeInformation
Write-Host "Detailed events exported to $detailedCsvFilePath"

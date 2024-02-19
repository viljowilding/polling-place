# get Chrome process
try {
    $chrome = Get-Process chrome
    if ($chrome) {
        $chrome.CloseMainWindow()
    }
    Remove-Variable chrome
}
catch {
    exit 1
}

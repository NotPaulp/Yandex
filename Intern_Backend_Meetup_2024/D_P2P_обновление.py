n, k = map(int, input().split())
downloaded = [[0] * (k + 1) for _ in range(n + 1)]
downloaded[1] = [0] + [1] * (k)
rarety = [0] + [n - 1] * (k)
value = [[0] * (n + 1) for _ in range(n + 1)]
chosenParts = [0] * (n + 1)
requiredTime = [0] * (n + 1)
time = 0
while sum(rarety) > 0:
    time += 1
    requests = [[] for i in range(n + 1)]

    for importDevice in range(2, n + 1):
        rarestPart = 0
        rarest = 0
        for part in range(1, k + 1):
            if rarety[part] > rarest and downloaded[importDevice][part] == 0:
                rarest = rarety[part]
                rarestPart = part


        if rarest == 0:
            continue

        chosenParts[importDevice] = rarestPart
        minParts = float('inf')
        currentExportDevice = 0
        for exportDevice in range(1, n + 1):
            if downloaded[exportDevice][rarestPart] == 1:
                parts = sum(downloaded[exportDevice])
                if parts < minParts:
                    minParts = parts
                    currentExportDevice = exportDevice
        if currentExportDevice == 0:
            continue
        requests[currentExportDevice].append(importDevice)

    for device in range(1, n + 1):
        requestingDevices = requests[device]
        maxValue = -1
        minParts = float('inf')
        mostValuableDevice = 0

        for requestingDevice in requestingDevices:
            requestingDeviceValue = value[device][requestingDevice]
            if requestingDeviceValue > maxValue:
                maxValue = requestingDeviceValue
                mostValuableDevice = requestingDevice
                minParts = sum(downloaded[requestingDevice])
            elif requestingDeviceValue == maxValue:
                parts = sum(downloaded[requestingDevice])
                if parts < minParts:
                    mostValuableDevice = requestingDevice
                    minParts = parts

        if mostValuableDevice != 0:
            value[mostValuableDevice][device] += 1
            part = chosenParts[mostValuableDevice]
            downloaded[mostValuableDevice][part] = 1
            rarety[part] -= 1
            if sum(downloaded[device]) >= k:
                requiredTime[device] = time
print(*requiredTime[2:])

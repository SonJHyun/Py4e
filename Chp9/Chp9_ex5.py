fname = open("mbox-short.txt")
domains = dict()

for line in fname:
    line = line.rstrip()
    if not line.startswith('From '): continue

    words = line.split()
    full_email = words[1]

    atPos = full_email.find('@')

    domainName = full_email[atPos+1:]
    if domainName not in domains:
        domains[domainName] = 1
    else:
        domains[domainName] += 1


print(domains)
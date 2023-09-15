#!/usr/bin/env python3

#########################################
# Fierce v0.1.1 - Beta 15/09/2023
#########################################


import argparse
import dns.resolver
import dns.query
import dns.zone

def main():
    parser = argparse.ArgumentParser(description='Fierce DNS Scanner')
    parser.add_argument('-o', '--output', help='Output file to save results')
    args = parser.parse_args()

    target_domain = input("Digite o domínio que deseja escanear: ")
    output_file = args.output

    if not target_domain:
        print("O domínio é obrigatório.")
        return

    # Perform DNS query to get authoritative nameservers
    authoritative_ns = get_authoritative_nameservers(target_domain)

    if not authoritative_ns:
        print("Falha ao encontrar servidores de nomes autoritativos.")
        return

    # Attempt zone transfer
    zone_data = attempt_zone_transfer(target_domain, authoritative_ns)

    if zone_data:
        print("Transferência de zona bem-sucedida. Exportando resultados para arquivo.")
        export_results(output_file, zone_data)
    else:
        print("A transferência de zona falhou. Realizando busca DNS por força bruta.")
        common_cnames = load_common_cnames()
        results = scan_dns(target_domain, authoritative_ns, common_cnames)
        if output_file:
            export_results(output_file, '\n'.join(results))
        else:
            for result in results:
                print(result)

def get_authoritative_nameservers(domain):
    try:
        resolver = dns.resolver.Resolver()
        resolver.timeout = 1
        resolver.lifetime = 1

        answers = resolver.query(domain, 'NS')
        authoritative_ns = [str(answer) for answer in answers]

        return authoritative_ns
    except Exception as e:
        print(f"Erro: {e}")
        return None

def attempt_zone_transfer(domain, nameservers):
    for ns in nameservers:
        try:
            zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
            zone_data = '\n'.join([str(record) for record in zone.iterate_rdatasets()])
            return zone_data
        except Exception as e:
            continue

    return None

def load_common_cnames():
    try:
        with open('common_cnames.txt', 'r') as file:
            common_cnames = [line.strip() for line in file.readlines()]
        return common_cnames
    except Exception as e:
        print(f"Erro ao carregar common_cnames.txt: {e}")
        return []

def scan_dns(domain, nameservers, common_cnames):
    results = []
    for ns in nameservers:
        for common_cname in common_cnames:
            target = f"{common_cname}.{domain}"
            try:
                answers = dns.resolver.query(target)
                for rdata in answers:
                    ip_address = rdata.address
                    results.append(f"{ip_address}\t{target}")
            except Exception as e:
                pass
    return results

def export_results(output_file, data):
    if output_file:
        with open(output_file, 'w') as file:
            file.write(data)
        print(f"Resultados exportados para {output_file}")

if __name__ == '__main__':
    main()

def analisar_log(arquivo_log):
    print("🛡️ INICIANDO VARREDURA BLUE TEAM 🛡️")
    print(f"Analisando: {arquivo_log}\n")

    tentativas_falhas = 0

    try:
        with open(arquivo_log, 'r') as log:
            for linha in log:
                if "Failed password" in linha or "authentication failure" in linha:
                    tentativas_falhas += 1
                    print(f"🚨 ALERTA: {linha.strip()}")

        print(f"\n📊 RELATÓRIO FINAL:")
        print(f"Total de tentativas de invasão detectadas: {tentativas_falhas}")

        if tentativas_falhas > 5:
            print("🔥 NÍVEL CRÍTICO! Possível ataque de força bruta!")
        elif tentativas_falhas > 0:
            print("⚠️ NÍVEL ATENÇÃO! Monitorar IPs suspeitos.")
        else:
            print("✅ Nenhuma ameaça detectada. Ambiente seguro.")

    except FileNotFoundError:
        print(f"❌ ERRO: Arquivo {arquivo_log} não encontrado.")

if __name__ == "__main__":
    analisar_log("teste.log")

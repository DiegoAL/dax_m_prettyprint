
def format_dax_file(input_file="daxcode.txt", output_file="daxcode_formatted.txt"):
    # Lê o conteúdo bruto do arquivo
    with open(input_file, "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Converte as sequências de escape literais (\n, \t) em quebras reais
    formatted_text = raw_text.encode("utf-8").decode("unicode_escape")

    # Salva no novo arquivo
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(formatted_text)

    print(f"✅ Código formatado salvo em: {output_file}")


if __name__ == "__main__":
    format_dax_file()

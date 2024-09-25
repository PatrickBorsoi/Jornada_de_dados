# %%
import os
import time
import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta

dotenv_path = "../../.env"
load_dotenv(dotenv_path)
USUARIO_SEI = os.getenv("USER")
SENHA_SEI = os.getenv("SENHA")
SEL_ORG = os.getenv("SEL_ORG")
SITE = os.getenv("SITE")

arquivo_tabela_mae = "../../../../workspace/00-database/Tabela Obras - SEIOP.xlsx"

df_tabela_mae = pd.read_excel(arquivo_tabela_mae)

# DATA
DATA = datetime.today()

DATA_ATUAL = DATA.strftime("%d-%m-%Y")

# %%
# Função para pegar o ultimo documento dos processos mae
erro = False
while erro == False:
    try:
        lista_id_obra = []
        lista_ultimo_doc = []
        lista_data_ult_doc = []
        lista_data_extracao = []
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get(SITE)

        time.sleep(1)
        # Recebendo os elementos
        username = driver.find_element(By.ID, "txtUsuario")
        password = driver.find_element(By.ID, "pwdSenha")
        select = Select(driver.find_element(By.ID, "selOrgao"))

        username.send_keys(USUARIO_SEI)
        password.send_keys(SENHA_SEI)
        select.select_by_value(SEL_ORG)

        password.submit()
        lista_teste = False
        while lista_teste == False:

            for obra in df_tabela_mae["Id Obra"]:
                # Retornando para o iframe padrão
                driver.switch_to.default_content()

                pesquisa = driver.find_element(By.ID, "txtPesquisaRapida")
                # SEI-330018/000256/2022 Testar o if do documento memoria de calculo
                pesquisa.send_keys(obra)
                pesquisa.submit()
                time.sleep(1)
                try:
                    msgSemAcesso = driver.find_element(By.ID, "divMensagem")
                    if msgSemAcesso.is_displayed():
                        msg_log_ = "Processo restrito"
                        lista_id_obra.append(obra)
                        lista_ultimo_doc.append(msg_log_)
                        lista_data_ult_doc.append(msg_log_)
                        lista_data_extracao.append(DATA_ATUAL)
                        continue
                except Exception as e:
                    pass

                # RESET_IFRAME = driver.switch_to.default_content()

                try:
                    IFRAME_ARVORE_ARQUIVO = driver.find_element(
                        By.CSS_SELECTOR, "#divIframeArvore > iframe"
                    )
                    driver.switch_to.frame(IFRAME_ARVORE_ARQUIVO)

                    LISTA_DOCUMENTOS = driver.find_elements(
                        By.CLASS_NAME, "infraArvoreNo"
                    )
                    if len(LISTA_DOCUMENTOS) != 0:
                        lista_invertida = reversed(LISTA_DOCUMENTOS)
                        nom_ultimo_arquivo = LISTA_DOCUMENTOS[-1].text
                    else:
                        LISTA_DOCUMENTOS = driver.find_element(
                            By.CLASS_NAME, "infraArvoreNo"
                        )
                        nom_ultimo_arquivo = LISTA_DOCUMENTOS.text
                except Exception as e:
                    print(e)
                    pass

                for documento in lista_invertida:
                    try:
                        driver.switch_to.default_content()
                        IFRAME_CONTEUDO_DOCUMENTO = driver.find_element(
                            By.CSS_SELECTOR, "#divIframeVisualizacao > iframe"
                        )
                        driver.switch_to.frame(IFRAME_CONTEUDO_DOCUMENTO)
                        IFRAME_CONTEUDO_BRANCO = driver.find_element(
                            By.CSS_SELECTOR,
                            "#divArvoreConteudo > #divArvoreHtml > #divArvoreInformacao",
                        )
                        pdf_texto = IFRAME_CONTEUDO_BRANCO.text
                        check_text = pdf_texto.find("Clique aqui")
                        if check_text == 0:
                            break
                    except Exception:
                        pass
                    data_doc = ""
                    driver.switch_to.default_content()
                    IFRAME_ARVORE_ARQUIVO = driver.find_element(
                        By.CSS_SELECTOR, "#divIframeArvore > iframe"
                    )
                    driver.switch_to.frame(IFRAME_ARVORE_ARQUIVO)
                    nome_documento = documento.text
                    nome_anexo_encontrado = nome_documento.find("Anexo Memória")
                    # if nome_anexo_encontrado == 0:
                    #    documento = next(lista_invertida)
                    #    nome_documento = documento.text
                    documento.click()

                    driver.switch_to.default_content()
                    IFRAME_CONTEUDO_DOCUMENTO = driver.find_element(
                        By.CSS_SELECTOR, "#divIframeVisualizacao > iframe"
                    )
                    driver.switch_to.frame(IFRAME_CONTEUDO_DOCUMENTO)

                    try:
                        IFRAME_CONTEUDO_BRANCO = driver.find_element(
                            By.CSS_SELECTOR,
                            "#divArvoreConteudo > #divArvoreHtml > #divArvoreInformacao",
                        )
                        processo_not_click_texto = IFRAME_CONTEUDO_BRANCO.text
                        processo_not_click_nao_possui = processo_not_click_texto.find(
                            "Processo não possui"
                        )
                        processo_not_click_nao_aberto = processo_not_click_texto.find(
                            "Processo aberto"
                        )
                        processo_not_click_nao_contem_anexo = (
                            processo_not_click_texto.find("Processo")
                        )
                        texto_pdf = processo_not_click_texto.find("Clique aqui")
                        if texto_pdf == 0:
                            break
                        n = 1
                        if (
                            processo_not_click_nao_possui == 0
                            or processo_not_click_nao_aberto == 0
                            or processo_not_click_nao_contem_anexo == 0
                        ):
                            driver.switch_to.default_content()
                            driver.switch_to.frame(IFRAME_ARVORE_ARQUIVO)
                            try:
                                xpath_pattern = '//*[@id[starts-with(., "ancjoin")]]'
                                if xpath_pattern:
                                    botao_mais = driver.find_elements(
                                        By.XPATH, xpath_pattern
                                    )[-2].click()
                            except Exception:
                                pass
                            driver.switch_to.default_content()
                            driver.switch_to.frame(IFRAME_CONTEUDO_DOCUMENTO)
                            while IFRAME_CONTEUDO_BRANCO:
                                driver.switch_to.default_content()
                                driver.switch_to.frame(IFRAME_ARVORE_ARQUIVO)
                                time.sleep(1.5)
                                LISTA_DOCUMENTOS = driver.find_elements(
                                    By.CLASS_NAME, "infraArvoreNo"
                                )
                                LISTA_DOCUMENTOS[-n].click()
                                nome_documento = LISTA_DOCUMENTOS[-n].text

                                driver.switch_to.default_content()
                                driver.switch_to.frame(IFRAME_CONTEUDO_DOCUMENTO)
                                IFRAME_CONTEUDO_BRANCO = driver.find_element(
                                    By.CSS_SELECTOR,
                                    "#divArvoreConteudo > #divArvoreHtml > #divArvoreInformacao",
                                )
                                texto_cpf = IFRAME_CONTEUDO_BRANCO.text
                                texto_pdf = texto_cpf.find("Clique aqui")
                                if texto_pdf == 0:
                                    break
                                n += 1
                        else:
                            break
                    except Exception as e:
                        pass

                    try:
                        IFRAME_ARVORE_ARQUIVO_DOC = driver.find_element(
                            By.CSS_SELECTOR,
                            "#divArvoreConteudo > #divArvoreHtml > iframe",
                        )
                        if IFRAME_ARVORE_ARQUIVO_DOC:
                            driver.switch_to.frame(IFRAME_ARVORE_ARQUIVO_DOC)
                            assinatura = driver.find_element(By.XPATH, "/html/body")
                            assinatura_text = assinatura.text
                            inicio = assinatura_text.find(
                                "Documento assinado eletronicamente por"
                            )
                            fim = assinatura_text.find(", às")
                            data_doc = assinatura_text[inicio:fim]
                            data_doc = data_doc[-10:]
                            if data_doc == "":
                                continue
                            driver.switch_to.default_content()
                            if data_doc != "":
                                break
                    except Exception as e:
                        # print(e)
                        break
                try:
                    if data_doc == "":
                        driver.switch_to.default_content()
                        driver.switch_to.frame(IFRAME_CONTEUDO_DOCUMENTO)
                        IFRAME_ARVORE_ARQUIVO_PDF = driver.find_element(
                            By.CSS_SELECTOR,
                            "#divArvoreConteudo > #divArvoreHtml > #divArvoreInformacao",
                        )
                        if IFRAME_ARVORE_ARQUIVO_PDF:
                            botao_click = driver.find_element(
                                By.XPATH, '//*[@id="divArvoreAcoes"]/a[1]'
                            )
                            botao_click.click()
                            time.sleep(1)
                            data_doc = driver.find_element(
                                By.XPATH, '//*[@id="tblAnexos"]/tbody/tr/td[3]/div'
                            ).text
                            data_doc = data_doc[:10]
                except Exception as e:
                    # print(e)
                    break

                lista_ultimo_doc.append(nome_documento)
                lista_data_ult_doc.append(data_doc)
                lista_id_obra.append(obra)
                lista_data_extracao.append(DATA_ATUAL)
                print(
                    f"{len(lista_ultimo_doc)} | {len(lista_data_ult_doc)} | {len(lista_id_obra)} \n {nome_documento} | {data_doc} | {obra}"
                )

            if (
                len(lista_data_extracao)
                == len(lista_data_ult_doc)
                == len(lista_id_obra)
                == len(lista_ultimo_doc)
            ):
                lista_teste = True
                driver.quit()

        erro = True
    except Exception as e:
        erro = False
        driver.quit()


lista_num_ultimo_doc = []
for documento in lista_ultimo_doc:
    verifica_parenteses = documento.find(")")
    if verifica_parenteses != -1:
        num_doc = documento[-9:-1]
        lista_num_ultimo_doc.append(num_doc)
    elif documento == "Processo restrito":
        num_doc = "Processo restrito"
        lista_num_ultimo_doc.append(num_doc)
    else:
        num_doc = documento[-8:]
        lista_num_ultimo_doc.append(num_doc)
    print(f"numero do documento: {documento} ultimo numero: {num_doc}")

# %%
df_ultimo_doc = {
    "Id Obra": lista_id_obra,
    "ultimo_documento": lista_ultimo_doc,
    "data_doc": lista_data_ult_doc,
    "numero_documento": lista_num_ultimo_doc,
    "data da extração": lista_data_extracao,
}
df_tabela_mae_ultimo_doc = pd.DataFrame(df_ultimo_doc)
df_tabela_mae_ultimo_doc
df_tabela_mae_fase = df_tabela_mae[["Id Obra", " FASE"]]
df_tabela_mae_ultimo_doc_fase = pd.merge(
    df_tabela_mae_fase, df_tabela_mae_ultimo_doc, how="right", on=["Id Obra"]
)
df_tabela_mae_ultimo_doc_fase

df_tabela_mae_ultimo_doc_fase.to_excel(
    f"../../../../workspace/00-database/processo_mae/lista_completa/lista_{DATA_ATUAL}.xlsx",
    index=False,
)
# %%
# VERIFICAÇÃO DO DIA ANTERIOR
# dia da semana(0=segunda, 1=Terça, 2=Quarta, 3=Quinta, 4=sexta, 5=sabado, 6=domingo)
dia_semana = DATA.weekday()
nomes = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
if dia_semana == 0:
    print(f"Dia da semana: {nomes[dia_semana]}")
    diferenca = timedelta(days=3)
else:
    print(f"Dia da semana: {nomes[dia_semana]}")
    diferenca = timedelta(days=1)

dia_anterior = DATA - diferenca
dia_anterior = dia_anterior.strftime("%d-%m-%Y")

print(f"Data dia anterior: {dia_anterior}")


lista_completa_dia_anterior = pd.read_excel(
    f"../../../../workspace/00-database/processo_mae/lista_completa/lista_{dia_anterior}.xlsx"
)
lista_completa_dia_anterior

# %%
# COMPARANDO AS LISTAS DO DIA ANTERIOR COM A ATUAL
comparativo = pd.merge(
    lista_completa_dia_anterior,
    df_tabela_mae_ultimo_doc_fase,
    how="right",
    on=["ultimo_documento"],
    suffixes=["_anterior", None],
    indicator=True,
).dropna(inplace=False, axis=1, how="all")
comparativo

colunas_para_manter = [
    col for col in comparativo.columns if not col.endswith("anterior")
]
comparativo = comparativo[colunas_para_manter]
comparativo

verificacao_novos_arquivos = comparativo[comparativo["_merge"] != "both"].drop(
    columns=["_merge"]
)
verificacao_novos_arquivos

arquivo_tabela_mae_alteracao = f"../../../../workspace/00-database/processo_mae/lista_comparativa/lista_processo_mae_{DATA_ATUAL}.xlsx"
verificacao_novos_arquivos.to_excel(arquivo_tabela_mae_alteracao, index=False)
# %%
"""Verificar esse ID:  33001/001230/2024
olhar esse sei é concertar na lsita
SEI-330001/001468/2024
"""

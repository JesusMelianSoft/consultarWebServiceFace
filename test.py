from ServiceFace import *

face = ServiceFace()

##FIRMAR XML
# fileContent = '{"FileHeader":{"SchemaVersion":"3.2","Modality":"I","InvoiceIssuerType":"EM","Batch":{"BatchIdentifier":"B38031241ABCLIS-URG","InvoicesCount":"1","TotalInvoicesAmount":{"TotalAmount":"-119.90"},"TotalOutstandingAmount":{"TotalAmount":"-119.90"},"TotalExecutableAmount":{"TotalAmount":"-119.90"},"InvoiceCurrencyCode":"EUR"}},"Parties":{"SellerParty":{"TaxIdentification":{"PersonTypeCode":"J","ResidenceTypeCode":"R","TaxIdentificationNumber":"B38031241"},"AdministrativeCentres":{"AdministrativeCentre":{"CentreCode":"H005","Name":"RAFAEL","FirstSurname":"MARTÃNEZ","SecondSurname":"ITURBE","AddressInSpain":{"Address":"PLAYA DE LAS AMERICAS","PostCode":"38660","Town":"ARONA","Province":"38","CountryCode":"ESP"}}},"LegalEntity":{"CorporateName":"ClÃ­nicas del Sur S.L.U.","TradeName":"HOSPITEN SUR","AddressInSpain":{"Address":"PLAYA DE LAS AMERICAS","PostCode":"38660","Town":"ARONA","Province":"38","CountryCode":"ESP"}}},"BuyerParty":{"TaxIdentification":{"PersonTypeCode":"J","ResidenceTypeCode":"R","TaxIdentificationNumber":"B38031241"},"AdministrativeCentres":[{"AdministrativeCentre":{"CentreCode":"","RoleTypeCode":"01","Name":"","AddressInSpain":{"Address":"","PostCode":"","Town":"","Province":"","CountryCode":"ESP"},"CentreDescription":""}},{"AdministrativeCentre":{"CentreCode":"","RoleTypeCode":"02","Name":"","AddressInSpain":{"Address":"","PostCode":"","Town":"","Province":"","CountryCode":"ESP"},"CentreDescription":""}},{"AdministrativeCentre":{"CentreCode":"","RoleTypeCode":"03","Name":"","AddressInSpain":{"Address":"","PostCode":"","Town":"","Province":"","CountryCode":"ESP"},"CentreDescription":""}}],"LegalEntity":{"CorporateName":"SERVICIO CANARIO DE SALUD (TENERIFE)","TradeName":"SERVICIO CANARIO DE SALUD (TENERIFE)","AddressInSpain":{"Address":"MENDEZ NUÃ‘EZ,14","PostCode":"38003","Town":"SANTA CRUZ DE TENERI","Province":"38","CountryCode":"ESP"}}}},"Invoices":{"Invoice":{"InvoiceHeader":{"InvoiceNumber":"0012345678","InvoiceSeriesCode":"ABCLIS-URG","InvoiceDocumentType":"FC","InvoiceClass":"OO"},"InvoiceIssueData":{"IssueDate":"2022-11-04","InvoiceCurrencyCode":"EUR","TaxCurrencyCode":"EUR","LanguageName":"es"},"TaxesOutputs":{"Tax":{"TaxTypeCode":"01","TaxRate":"0.00","TaxableBase":{"TotalAmount":"-119.90"},"TaxAmount":{"TotalAmount":"0.00"}}},"InvoiceTotals":{"TotalGrossAmount":"-119.90","TotalGeneralDiscounts":"0.00","TotalGeneralSurcharges":"0.00","TotalGrossAmountBeforeTaxes":"-119.90","TotalTaxOutputs":"0.00","TotalTaxesWithheld":"0.00","InvoiceTotal":"-119.90","TotalOutstandingAmount":"-119.90","TotalExecutableAmount":"-119.90"},"Items":[{"InvoiceLine":{"ReceiverTransactionReference":"0000000000","ItemDescription":"MI DESCR","Quantity":"1.000","UnitOfMeasure":"01","UnitPriceWithoutTax":"-119.900000","TotalCost":"-119.900000","GrossAmount":"-119.900000","TaxesOutputs":{"Tax":{"TaxTypeCode":"01","TaxRate":"0.00","TaxableBase":{"TotalAmount":"0.00"},"TaxAmount":{"TotalAmount":"0.00"}}},"SpecialTaxableEvent":{"SpecialTaxableEventCode":"01","SpecialTaxableEventReason":"SCS"}}}]}}} '
# invSigned = face.getInvoiceSigned(pCert = 'clis', pAlias = '45438263s_juan_carlos_perez__r:_b38031241_', pFileContent = fileContent)
# print(invSigned)

##ENVIAR FACTURA
# res = face.sendInvoice(face.getInvoiceSigned(pCert = 'clis', pAlias = '45438263s_juan_carlos_perez__r:_b38031241_', pFileContent = fileContent), 'jdmelian@hospiten.com')
# print(res)


##ANULAR FACTURA
# res = face.anularFactura('REGAGE22e00053343922', 'error')
# if (res.resultado.codigo == '0'):
#     print(res.factura.mensaje + ': ' + res.factura.numeroRegistro)

##CONSULTAR ESTADO
# res = face.getStatus('REGAGE22e00053343922')
# print(res)
# if (res.resultado.codigo == '0'):
#     print(res.factura.anulacion.descripcion + ': ' + res.factura.numeroRegistro)


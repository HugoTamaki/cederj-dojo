
exports.saque = function(valor) {
  var streturn= [],
      contaNota = 0;
  if (valor % 10 != 0) {
    return "Digite um valor válido"}
  else{

    valor = contaNotas(streturn, valor, 100, "R$100,00");
    valor = contaNotas(streturn, valor, 50, "R$50,00");
    valor = contaNotas(streturn, valor, 20, "R$20,00");
    valor = contaNotas(streturn, valor, 10, "R$10,00");
    return streturn.join(" e ");
  }
}

function contaNotas(arrayNotas, valorAtual, valorNota, notaStr) {
  var contaNota = 0;

  while (valorAtual >= valorNota){
    valorAtual -= valorNota;
    contaNota += 1;
  }

  if (contaNota == 1) {
    arrayNotas.push("1 nota de "+notaStr);
  } else if (contaNota > 1) {
    arrayNotas.push(contaNota + " notas de "+notaStr);
  }
  return valorAtual;
}

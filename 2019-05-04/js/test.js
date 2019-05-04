var assert = require('assert');
var caixa = require('./dojo');

describe('Caixa Eletronico', function() {
  it('retorna R$ 20,00', function() {
    assert.equal(caixa.saque(20), "1 nota de R$20,00");
  });

  it('retorna R$ 30,00', function(){
    assert.equal(caixa.saque(30), "1 nota de R$20,00 e 1 nota de R$10,00");
  })

  it('retorna R$ 40,00', function(){
    assert.equal(caixa.saque(40), "2 notas de R$20,00");
  })

  it('retorna R$ 50,00', function(){
    assert.equal(caixa.saque(50), "1 nota de R$50,00");
  })

  it('retorna R$ 60,00', function(){
    assert.equal(caixa.saque(60), "1 nota de R$50,00 e 1 nota de R$10,00");
  });

  it('retorna R$ 100,00', function() {
    assert.equal(caixa.saque(100), "1 nota de R$100,00");
  });

  it('retorna R$ 180,00', function() {
    assert.equal(caixa.saque(180), "1 nota de R$100,00 e 1 nota de R$50,00 e 1 nota de R$20,00 e 1 nota de R$10,00");
  });

  it('retorna R$ 5,00', function() {
    assert.equal(caixa.saque(5), "Digite um valor válido");
  });


});
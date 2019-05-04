require './dojo'

describe 'sum' do
  it 'returns 2 when 1 + 1' do
    expect(sum(1, 1)).to eql(2)
  end
end
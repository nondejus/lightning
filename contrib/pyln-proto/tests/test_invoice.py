from pyln.proto import Invoice
from decimal import Decimal
from bitstring import ConstBitStream


def test_decode():
    i = 'lnbcrt1u1p0zyt04pp5wcnjhxu4k98td0kw8ng9zqrd3246cc7r559a063tk5mp9v9fxf9sdpqw3jhxazlwpshjhmjda6hgetzdahhxapjxqyjw5qcqp9sp5asxa9pwxt6yuse5egtcna8gezazr657chz72qfzztsthxwnwj0yqr9yqdwjkyvjm7apxnssu4qgwhfkd67ghs6n6k48v6uqczgt88p6tky96qqqdcqqqqgqqyqqqqlgqqqqqzsqqcpc9njea0cche7cgemu9c6lyv55hxvjem9f2jgle799d3kt9kw7rxgqqphqqqqzqqqsqqqraqqqqqq2qqrq9qy9qsqfm47uq6ny374m22dxw7p6j8c0khj4tspjcj78l33vf6qv8grhknsmw6slxxucpvxv5s9464qfng8324sagn8g8ng3uuh4d2vdpnmsdgqyqhn4k'
    inv = Invoice.decode(i)

    assert(inv.hexpubkey == '032cf15d1ad9c4a08d26eab1918f732d8ef8fdc6abb9640bf3db174372c491304e')
    assert(inv.hexpaymenthash == '76272b9b95b14eb6bece3cd051006d8aabac63c3a50bd7ea2bb53612b0a9324b')
    assert(inv.min_final_cltv_expiry == 5)
    assert(inv.amount == Decimal('0.000001'))
    assert(inv.featurebits == ConstBitStream('0x28200'))
    print(inv)

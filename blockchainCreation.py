import block
import blockchain

chain = blockchain.Blockchain()

first = block.Block('first')
second = block.Block('second')
third = block.Block('third')

chain.add_block(first)
chain.add_block(second)
chain.add_block(third)

first.update_data('so broke')
print('Tried to update first block\n')
print('To check if blockchain is broken'+str(chain.broken)+'\n')  # True

chain.repair()

print('To check if blockchain is broken after repair'+str(chain.broken)+'\n')  # False

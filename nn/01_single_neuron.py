# This function simulates a single neuron: it takes some inputs,
# weighs how important each one is, adds a constant bias, and
# returns the result. This is the core building block every
# neural network is made of.
def neuron(inputs, weights, bias):
    total = 0
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    total += bias
    return total

result = neuron(inputs=[1.0, 2.0], weights=[0.5, -0.5], bias=1.0)
print(result)

# Adds a "bend" after the neuron's raw output, so the network can learn
# more than just straight-line relationships. ReLU is one of the
# simplest activation functions: negative numbers become 0, everything
# else stays the same.
def relu(x):
    if x < 0:
        return 0
    return x

activated_result = relu(result)
print(activated_result)
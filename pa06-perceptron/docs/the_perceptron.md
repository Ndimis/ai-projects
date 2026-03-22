# Concept Explainer: The Perceptron (The Biological Neuron of AI)

### 🧠 The Core Concept
The **Perceptron** is the "Hello World" of Neural Networks. It is a fundamental algorithm for supervised learning of binary classifiers—systems that can decide whether an input belongs to one class or another (e.g., "Normal Traffic" vs. "Malicious Traffic").

It mimics the biological neuron in a simplified mathematical form:
1.  **Inputs ($x$):** The raw data features (e.g., Packet Size, Request Frequency).
2.  **Weights ($w$):** The importance assigned to each input.
3.  **Summation:** The weighted inputs are added together plus a **Bias ($b$)**.
4.  **Activation Function:** If the sum exceeds a certain threshold (usually 0), the neuron "fires" an output of 1; otherwise, it outputs 0.

[Image of a single layer perceptron diagram showing inputs, weights, summation, and activation function]

The mathematical operation is:
$$\hat{y} = f(\sum_{i=1}^{n} w_i x_i + b)$$

### 🛠️ Lessons Learned
1.  **The Learning Rate ($\eta$):** This is a small positive value (e.g., 0.01) that determines how drastically we change the weights when the model makes a mistake. If the model is too "stubborn," it learns slowly; if it is too "jumpy," it never settles on a solution.
2.  **Linear Separability:** A single Perceptron can only solve problems where a single straight line can separate the two classes. It cannot solve non-linear problems like the XOR gate—this limitation eventually led to the creation of Multi-Layer Neural Networks (Deep Learning).
3.  **The Perceptron Update Rule:** We only adjust the weights when the prediction is wrong. The formula $w = w + \eta(target - prediction) \times input$ ensures the weights move in a direction that reduces the error for that specific input.

### 📝 Key Takeaway
> **Deep Learning starts here.** While a single neuron is limited, connecting thousands of them in layers allows AI to recognize faces, translate languages, and detect complex cyberattacks. Understanding the Perceptron is the key to demystifying how "machines learn."

### 🚀 How to Run

1. **Install Dependencies**:
   Ensure you have the core math libraries:
   ```bash
   pip install -r requirements.txt
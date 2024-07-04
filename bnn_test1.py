import tensorflow as tf
import tensorflow_probability as tfp
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

tfd = tfp.distributions

# 生成数据
def generate_data(n=100):
    x = np.linspace(-3, 3, n)
    y = 0.5 * x + np.random.normal(size=n)
    x = (x - np.mean(x)) / np.std(x)  # 标准化处理
    return x, y

# 定义BNN模型
def build_bnn():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(256, activation='relu'),
        tfp.layers.DenseFlipout(256, activation='relu'),
        tfp.layers.DenseFlipout(1)
    ])
    return model

# 训练BNN模型
def train_bnn(model, x_train, y_train):
    x_train = np.expand_dims(x_train, axis=-1)  # 重塑输入数据
    print("Training model...")
    model.compile(optimizer='adam', loss='mse')
    model.fit(x_train, y_train, epochs=5000, verbose=1)
    print("Model training complete.")

# 验证和绘图
def plot_results(model, x_test, y_test):
    x_test = np.expand_dims(x_test, axis=-1)  # 重塑输入数据
    y_pred = model(x_test)
    plt.scatter(x_test, y_test, label='True data')
    plt.scatter(x_test, y_pred, label='Predicted data')
    plt.legend()
    plt.show()
    print("Plot generated.")

# 主函数
if __name__ == "__main__":
    x_train, y_train = generate_data()
    print("Data generated.")
    model = build_bnn()
    print("Model built.")
    train_bnn(model, x_train, y_train)
    print("Model trained.")
    plot_results(model, x_train, y_train)
    print("Results plotted.")
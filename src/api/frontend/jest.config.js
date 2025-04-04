export default {
  transform: {
    '^.+\\.vue$': '@vue/vue3-jest', // Transforma arquivos .vue
    '^.+\\.js$': 'babel-jest', // Transforma arquivos .js
  },
  moduleFileExtensions: ['js', 'json', 'vue'], // Extensões de arquivos suportadas
  testEnvironment: 'jest-environment-jsdom', // Ambiente de teste
  transformIgnorePatterns: [
    '/node_modules/(?!axios)', // Transforma dependências específicas, se necessário
  ],
};
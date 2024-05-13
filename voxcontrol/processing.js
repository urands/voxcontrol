export async function processingCommand(command) {
  const selector = command.selector;
  if (
    !command ||
    !command.selector ||
    !command.attribute ||
    typeof command.value === 'undefined'
  ) {
    console.error('Необходимо предоставить selector, attribute и value.');
    return;
  }
  const elements = document.querySelectorAll(command.selector);
  // Если элементы не найдены, выводим предупреждение
  if (elements.length === 0) {
    console.warn('Элементы по указанному селектору не найдены.');
    return;
  }

  // Обновляем атрибут для каждого элемента
  elements.forEach((element) => {
    element.setAttribute(command.attribute, command.value);
  });

  console.log(
    `Атрибут ${command.attribute} обновлён для ${elements.length} элементов.`
  );
}

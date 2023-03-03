function onDragOver(event) {
    event.preventDefault();
  }


function onDragStart(event) {
    event
      .dataTransfer
      .setData('text/plain', event.target.id);
  
    event
      .currentTarget
      .style
      .backgroundColor = '#FFF';
  }


  function onDrop(event) {
    const id = event
      .dataTransfer
      .getData('text');

      const draggableElement = document.getElementById(id);
      const dropzone = event.target;
      consoleLog(draggableElement);
      dropzone.appendChild(draggableElement);

      event
        .dataTransfer
        .clearData();
  }
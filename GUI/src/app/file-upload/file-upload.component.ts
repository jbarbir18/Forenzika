import { Component } from '@angular/core';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent {
  fileDropped: boolean = false;

  constructor() {}

  onDrop(event: DragEvent) {
    event.preventDefault();
    this.fileDropped = true;
    let files = event.dataTransfer?.files;
    if (files && files.length > 0) {
      this.handleFiles(files);
    }
  }

  onDragOver(event: DragEvent) {
    event.preventDefault();
  }

  onDragLeave(event: DragEvent) {
    event.preventDefault();
  }

  handleFiles(files: FileList) {
    // handle the file here
  }
}

import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { TextToSqlService } from '../../services/text-to-sql.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-chatdb',
  standalone: true,
  imports: [CommonModule, FormsModule,
            MatCardModule, MatButtonModule, MatIconModule],
  templateUrl: './chatdb.component.html',
  styleUrl: './chatdb.component.css',
  providers: [TextToSqlService]
})
export class ChatdbComponent {
  question: string = '';
  responseData: any;

  constructor(private textToSqlService: TextToSqlService) {}

  // Function to handle question submission
  submitQuestion(): void {
    if (this.question.trim()) {
      this.textToSqlService.getSqlQuery(this.question).subscribe(
        (response) => {
          this.responseData = response;
        },
        (error) => {
          console.error('Error:', error);
        }
      );
    }
  }
}

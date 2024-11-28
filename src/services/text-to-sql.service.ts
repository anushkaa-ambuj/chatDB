import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TextToSqlService {
  private apiUrl = 'http://127.0.0.1:8000/api/text-to-sql/';

  constructor(private http: HttpClient) {}

  // Function to send question to Django API
  getSqlQuery(question: string): Observable<any> {
    return this.http.post<any>(this.apiUrl, { question });
  }
}

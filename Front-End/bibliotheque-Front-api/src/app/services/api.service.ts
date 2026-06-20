import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Opinion } from '../models/Opinion';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private url: string = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {} // element qui nous permet d'effectuer des appel api

  getAllOpinions() {
    return this.http.get<Array<Opinion>>(this.url + '/Avis/');
  }
}

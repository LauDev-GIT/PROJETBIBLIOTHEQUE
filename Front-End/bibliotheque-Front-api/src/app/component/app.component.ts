import { HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ApiService } from '../services/api.service';
import { NavComponent } from '../component/nav/nav.component'; // Chemin à adapter
import { provideAnimations } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { Opinion } from '../models/Opinion';
import { OpinionComponent } from './opinion/opinion.component';

@Component({
  selector: 'bfa-root',
  standalone: true,
  imports: [
    OpinionComponent,
    NavComponent,
    RouterOutlet,
    MatButtonModule,
    HttpClientModule,
  ],
  providers: [ApiService, provideAnimations()],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent implements OnInit {
  title = 'bibliotheque-Front-api';

  opinions: Array<Opinion> = [];

  constructor(private apiService: ApiService) {
    //ngOnInit(): void
    //  alert('Hi Guy!');
  }

  //ici on va effectuerf le traitement
  ngOnInit() {
    this.apiService.getAllOpinions().subscribe((data) => {
      this.opinions = data;
      console.log(this.opinions);
    });
  }
}
export class AppCompnent {}

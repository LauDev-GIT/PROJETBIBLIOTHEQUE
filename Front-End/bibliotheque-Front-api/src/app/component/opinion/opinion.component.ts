import { Component, OnInit } from '@angular/core';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { RouterOutlet } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'bfa-opinion',
  standalone: true,
  imports: [
    MatButtonModule,
    MatInputModule,
    RouterOutlet,
    MatProgressSpinnerModule,
  ], // 👈 IMPORTANT
  templateUrl: './opinion.component.html',
  styleUrls: ['./opinion.component.css'],
})
export class OpinionComponent implements OnInit {
  isLoading: boolean = true;

  ngOnInit() {
    alert("Hey! Guy What's up");
  }
  constructor() {
    // Simule un chargement
    setTimeout(() => {
      this.isLoading = false;
    }, 3000);
  }
}

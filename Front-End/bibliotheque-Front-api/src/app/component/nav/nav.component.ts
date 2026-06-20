import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'bfa-nav',
  standalone: true,
  imports: [RouterLink, RouterLinkActive, MatButtonModule, MatInputModule],
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css'],
})
export class NavComponent {
  logoPath: string = 'assets/images/Bibliotheque.png';
}

import { Routes } from '@angular/router';
import { OpinionComponent } from './component/opinion/opinion.component';
import { AppCompnent } from './component/app.component';

export const routes: Routes = [
  {
    path: 'opinion',
    component: OpinionComponent,
  },
  {
    path: '**',
    component: AppCompnent,
  },
];

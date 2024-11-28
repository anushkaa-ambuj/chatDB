import { TestBed } from '@angular/core/testing';

import { TextToSqlService } from './text-to-sql.service';

describe('TextToSqlService', () => {
  let service: TextToSqlService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TextToSqlService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
